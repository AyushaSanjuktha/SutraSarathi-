import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity
from pyngrok import ngrok

# Step 1: Load Datasets
print("Loading datasets...")
gita_df = pd.read_csv("Bhagwad_Gita_Verses_English_Questions.csv")  # Bhagavad Gita dataset
pys_df = pd.read_csv("Patanjali_Yoga_Sutras_Verses_English_Questions.csv")  # Patanjali Yoga Sutras dataset

# Add source information
gita_df['Source'] = 'Bhagavad Gita'
pys_df['Source'] = 'Patanjali Yoga Sutras'

# Merge datasets
combined_df = pd.concat([gita_df, pys_df], ignore_index=True)
combined_df['Text'] = combined_df['translation']  # Ensure consistent column names
combined_df.fillna('', inplace=True)  # Handle missing values

# Step 2: Initialize Sentence Transformer for Embedding
print("Initializing Sentence Transformer...")
model_name = "multi-qa-mpnet-base-dot-v1"
embedder = SentenceTransformer(model_name)

# Generate embeddings for the combined dataset
print("Generating embeddings...")
embeddings = embedder.encode(combined_df['Text'].tolist(), convert_to_tensor=False)

# Step 3: Create FAISS Index
print("Creating FAISS index...")
dimension = embeddings[0].shape[0]  # Dimension of embeddings
index = faiss.IndexFlatL2(dimension)  # L2 distance (Euclidean)
index.add(np.array(embeddings))  # Add embeddings to the index

# Save the FAISS index for reuse
faiss.write_index(index, "combined_faiss_index")

# Step 4: Load Pre-trained Language Model
print("Loading language model...")
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
language_model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m")

# Step 5: Define Query Function
def compute_accuracy(query, retrieved_texts):
    """Compute cosine similarity between query and retrieved texts."""
    query_embedding = embedder.encode([query], convert_to_tensor=False)
    retrieved_embeddings = embedder.encode(retrieved_texts, convert_to_tensor=False)
    similarities = cosine_similarity([query_embedding[0]], retrieved_embeddings)
    return similarities.max()

def query_pipeline(user_query):
    """Process user query to retrieve relevant texts."""
    # Handle casual greetings or non-query inputs
    greetings = ["hi", "hello", "hey", "namaste","hii"]
    if user_query.lower().strip() in greetings:
        return {
            "friendly_response": "Hello! How can I assist you today? You can ask about verses, teachings, or other related topics."
        }

    # Check for inappropriate keywords
    inappropriate_keywords = ["violence", "hate", "abuse", "sex"]
    if any(word in user_query.lower() for word in inappropriate_keywords):
        return {"error": "Inappropriate Query"}

    # Process the query for embedding search
    query_embedding = embedder.encode([user_query], convert_to_tensor=False)
    k = 3  # Number of top results to retrieve
    distances, indices = index.search(np.array([query_embedding[0]]), k)

    # Retrieve nearest texts
    try:
        retrieved_texts = combined_df.iloc[indices[0]]['Text'].tolist()
        sources = combined_df.iloc[indices[0]]['Source'].tolist()
        chapters = combined_df.iloc[indices[0]]['chapter'].tolist()
        titles = combined_df.iloc[indices[0]]['verse'].tolist()
    except IndexError:
        return {"error": "No relevant results found. Please refine your query."}

    # Filter results for relevance
    relevant_texts = []
    for text, title, chapter, source in zip(retrieved_texts, titles, chapters, sources):
        relevant_texts.append({"text": text, "title": title, "chapter": chapter, "source": source})

    if not relevant_texts:
        return {"error": "No relevant results found. Please refine your query."}

    # Take the most relevant result
    best_text = relevant_texts[0]["text"]

    # Generate a focused response based on the best match
    response = best_text

    # Compute accuracy
    accuracy_score = compute_accuracy(user_query, [best_text])
    return {
        "query": user_query,
        "retrieved_texts": relevant_texts,
        "generated_response": response,
        "accuracy_score": accuracy_score
    }

# Gradio Interface Function
def gradio_interface(user_query):
    # Call the query pipeline with the user's query
    result = query_pipeline(user_query)
    if "friendly_response" in result:
        return result["friendly_response"]

    if "error" in result:
        return result["error"]
    
    # Format the response text
    response = f"Query: {result['query']}\n"
    for idx, result_text in enumerate(result["retrieved_texts"]):
        response += f"\n\nResult {idx + 1}:\n"
        response += f"Text: {result_text['text']}\n"
        response += f"Source: {result_text['source']}\n"
        response += f"Chapter: {result_text['chapter']}\n"
        response += f"Title: {result_text['title']}\n"
    
    response += f"\nGenerated Response: {result['generated_response']}\n"
    response += f"Accuracy Score: {result['accuracy_score']:.4f}"
    
    return response

# Launch Gradio interface
interface = gr.Interface(fn=gradio_interface, inputs="text", outputs="text", title="Sutra saradhi")

# Set up the ngrok tunnel for sharing
public_url = ngrok.connect(7860)  # Default Gradio port is 7860
print(f"Public URL: {public_url.public_url}")

# Launch the Gradio app
interface.launch(server_name="0.0.0.0", server_port=7860, share=True)