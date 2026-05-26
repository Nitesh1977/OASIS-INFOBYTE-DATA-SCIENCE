import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from textblob import TextBlob

df=pd.read_csv("user_reviews.csv")
print(df.head(),df.info(),df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
df.dropna(inplace=True)
df.dropna(subset=['Translated_Review'], inplace=True)

df['Polarity'] = df['Translated_Review'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

df['Sentiment'] =df['Polarity'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

sns.countplot(x='Sentiment', data=df)
plt.title("Sentiment Analysis of Reviews")
plt.show()

