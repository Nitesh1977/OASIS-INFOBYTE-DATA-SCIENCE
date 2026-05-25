# IMPORT LIBRARIES

import pandas as pd
import re

df= pd.read_csv("Twitter_Data.csv")

#  Data Understanding
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# DATA CLEANING
df.dropna(inplace=True)
print(df.duplicated().sum())    
df.drop_duplicates(inplace=True)

# TEXT CLEANING FUNCTION
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text
df['clean_text'] = df['clean_text'].apply(clean_text)
df.to_csv("cleaned_twitter_data.csv", index=False)



