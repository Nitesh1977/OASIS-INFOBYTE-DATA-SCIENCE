import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv("apps.csv")
print(df.head(),df.info(),df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
df.dropna(inplace=True)
df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = df['Installs'].str.replace(',', '')
df['Installs'] = pd.to_numeric(df['Installs'])
df['Price'] = df['Price'].str.replace('$', '')  
df['Price'] = pd.to_numeric(df['Price'])

plt.figure(figsize=(12,6))
sns.countplot(y='Category', data=df)
plt.title("App Categories Distribution")
plt.savefig("App Categories Distribution.png")
plt.show()  

sns.histplot(df['Rating'], kde=True)
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.savefig("Ratings Distribution.png")
plt.show()

df.groupby('Category')['Installs'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top Categories by Installs")
plt.xlabel("Category")
plt.ylabel("Average Installs")
plt.savefig("Top Categories by Installs.png")
plt.show()

sns.countplot(x='Type', data=df)
plt.title("Free vs Paid Apps")
plt.savefig("Free vs Paid Apps.png")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("Correlation Heatmap.png")
plt.show()
    
import plotly.express as px

fig = px.scatter(df, 
                 x='Reviews', 
                 y='Rating',
                 color='Category',
                 hover_name='App',
                 title='Rating vs Reviews (Interactive)')
fig.show()