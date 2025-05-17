#  Sentiment Analysis on Amazon Product Reviews

This project performs sentiment analysis on Amazon product reviews using Python and TextBlob. The project applies AI-powered Natural Language Processing using TextBlob, a pre-trained sentiment analysis model, to classify Amazon product reviews as Positive, Negative, or Neutral, and visualizes the sentiment distribution using Matplotlib and Tableau.

---

##  Project Summary

- **Objective:** Analyze customer sentiment from real product reviews to understand public perception.
- **Dataset:** [Amazon Product Reviews (Datafiniti)](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products)
- **Tools Used:**
  - Python (Pandas, TextBlob, Seaborn, Matplotlib)
  - Jupyter Notebook / VS Code
  - Tableau Public

---

## Key Steps

- Loaded and cleaned review data from CSV
- Applied `TextBlob` for sentiment scoring (polarity)
- Classified reviews as **Positive**, **Neutral**, or **Negative**
- Saved the results to `sentiment_output.csv`
- Created:
  - Sentiment count bar chart (Python)
  - Interactive Tableau dashboard with sentiment filters and review table

---

## Skills Applied

- Natural Language Processing (NLP)
- Text classification
- Data cleaning and visualization
- Sentiment modeling using AI tools

---
### AI/NLP Workflow

- Used **TextBlob**, a pre-trained NLP model built on NLTK and Pattern
- Extracted **sentiment polarity scores** for each review
- Automatically classified review sentiment using AI logic:
  - Polarity > 0 → Positive
  - Polarity < 0 → Negative
  - Polarity = 0 → Neutral
