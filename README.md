# Sutra Sarathi

A semantic search application designed to retrieve and display relevant verses from the Bhagavad Gita and Patanjali Yoga Sutras based on user queries. This application includes an accuracy score for retrieved results and offers a user-friendly Gradio interface.

## Table of Contents
- [Introduction](#sutra-sarathi)
- [Features](#features)
- [Requirements](#requirements)
- [Files](#files)
- [Installation and Setup](#installation-and-setup)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Install Dependencies](#step-2-install-dependencies)
  - [Step 3: Ensure Dataset Files](#step-3-ensure-dataset-files)
  - [Step 4: Run the Application](#step-4-run-the-application)
  - [Step 5: Access the Gradio Interface](#step-5-access-the-gradio-interface)
- [Example Usage](#example-usage)
- [Submission Checklist](#submission-checklist)
- [Contributing](#contributing)
- [License](#license)
## Introduction
Sutra Sarathi enables users to explore ancient wisdom from the Bhagavad Gita and Patanjali Yoga Sutras effortlessly. The application serves as a bridge between modern technology and spiritual teachings, making these texts accessible to everyone.

## Features
- **Semantic Search**: Retrieve the most relevant verses based on natural language queries.
- **Accuracy Score**:Each result is accompanied by a confidence level (accuracy score) to indicate how closely it matches the user query, ensuring reliability and trustworthiness.
- **Interactive Interface**: Simple and intuitive Gradio-based user interface.

## Requirements
The following dependencies are required to run the application:

- Python 3.7+
- `pandas`
- `numpy`
- `sentence-transformers`
- `faiss-cpu`
- `transformers`
- `gradio`
- `scikit-learn`

## Files
1. **`app.py`** - Main Python script for running the application.
2. **`requirements.txt`** - List of dependencies.
3. **`Bhagwad_Gita_Verses_English_Questions.csv`** - Dataset containing verses from the Bhagavad Gita.
4. **`Patanjali_Yoga_Sutras_Verses_English_Questions.csv`** - Dataset containing verses from Patanjali Yoga Sutras.

## Installation and Setup
Follow these steps to set up and run the application:

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/AyushaSanjuktha/SutraSarathi-.git
cd SutraSarathi
```

### Step 2: Install Dependencies
Use the following command to install all required dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Ensure Dataset Files
Ensure `Bhagwad_Gita_Verses_English_Questions.csv` and `Patanjali_Yoga_Sutras_Verses_English_Questions.csv` are in the same directory as `app.py`. These files contain the Bhagavad Gita and Patanjali Yoga Sutras datasets.

### Step 4: Run the Application
Start the application by running:
```bash
python app.py
```

### Step 5: Access the Gradio Interface
- If running locally, open your browser and navigate to:
  ```
  http://127.0.0.1:7860
  ```
- If running on a cloud platform (e.g., Colab), use the public link provided by the app.

## How to Use

1. **Start the Application**:
   - Follow the steps in the [Installation and Setup](#installation-and-setup) section to run the application locally or in a cloud environment.

2. **Access the Gradio Interface**:
   - Open the provided URL (e.g., `http://127.0.0.1:7860` for local setups) in your web browser.

3. **Input Your Query**:
   - Enter your query in the input box on the Gradio interface. For example:
     ```text
     What is the meaning of life?
     ```

4. **View the Results**:
   - The application will retrieve the most relevant verse(s) from the Bhagavad Gita and Patanjali Yoga Sutras based on your query.
   - Results will include:
     - The retrieved text (verse)
     - Source (e.g., Bhagavad Gita or Patanjali Yoga Sutras)
     - Chapter and title (if available)
     - An accuracy score indicating the relevance of the result.

5. **Try More Queries**:
   - Experiment with different questions, such as:
     - "What is the path to enlightenment?"
     - "Explain the concept of karma."
     - "How to find inner peace?"
6. **Interpret the Results**:
   - Use the retrieved verses to gain insights or deeper understanding related to your query.

## Submission Checklist
1. **Files to Include**:
   - `app.py`
   - `requirements.txt`
   - `bs.csv`
   - `ps.csv`
   - `README.md`

2. **Testing**:
   - Ensure the application runs without errors.
   - Verify outputs for sample queries.

3. **GitHub Repository**:
   - Commit all files to a public or accessible private repository.
   - Verify the repository link before submission.

## Contributing
Contributions to Sutra Sarathi are welcome! Please follow these steps:

### Step 1: Fork the Repository
- Click the "Fork" button on the top right of the repository page to create your copy.

### Step 2: Clone the Forked Repository
```bash
git clone https://github.com/your-username/SutraSarathi.git
cd SutraSarathi
```

### Step 3: Create a New Branch
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-your-feature-name
```

### Step 4: Make Your Changes
- Update the code or documentation as needed.

### Step 5: Commit and Push Your Changes
```bash
git add .
git commit -m "Add your feature description"
git push origin feature-your-feature-name
```

### Step 6: Submit a Pull Request
- Navigate to the original repository and click "New Pull Request".
- Provide a clear description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

