# NLP Text Classification and Sentiment Analysis

## Overview
This project implements a Natural Language Processing (NLP) solution for text classification and sentiment analysis. The model categorizes user comments into predefined classes, enabling insights into user sentiments across various topics.

### Project Objectives
- Develop a machine learning model to classify text comments into one of ten classes.
- Create a user-friendly web application using Streamlit for real-time sentiment analysis.
- Allow users to input their comments and receive instant feedback on their sentiments.

## Dataset
- The dataset consists of **1799 samples** and includes the following **10 classes**:
  - **Sport**
  - **Shopping**
  - **Nourriture** (Food)
  - **Mode de vie** (Lifestyle)
  - **Culture**
  - **Bien-être** (Well-being)
  - **Loisir** (Leisure)
  - **Evénement** (Event)
  - **Industrie** (Industry)
  - **Voyage** (Travel)

### Features
- **Text Preprocessing**: The input text undergoes various preprocessing steps, including:
  - Removal of special characters and digits.
  - Lowercasing the text.
  - Removal of stopwords (common words that add little value).
- **TF-IDF Vectorization**: Converts the processed text into a numerical format suitable for model training.

## Machine Learning Models
The project implements multiple machine learning algorithms, including:
- **Multi-Layer Perceptron (MLP)**
- **Support Vector Machines (SVM)**
- **Naive Bayes Classifier**

Each model is evaluated, and the best-performing model is saved for use in the Streamlit application.

## Streamlit Web Application
The application allows users to input comments and receive sentiment predictions in real time.

### Key Features
- User input handling.
- Text preprocessing and transformation using the trained vectorizer.
- Display of sentiment predictions.

## Installation
To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NLP_Project.git
   cd NLP_Project
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Running the Application
   ```bash
   streamlit run src/sentiment_analysis_app.py

