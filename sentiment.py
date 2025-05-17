import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('amazon_reviews.csv', encoding='latin-1', low_memory=False)

print(df.columns)

df = df[['reviews.text']].dropna().rename(columns={'reviews.text': 'Review'})

# Analyze sentiment
df['Polarity'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['Sentiment'] = df['Polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Save output
df.to_csv("sentiment_output.csv", index=False)

# Visualize
sns.countplot(x='Sentiment', data=df)
plt.title("Sentiment Breakdown of Reviews")
plt.show()



