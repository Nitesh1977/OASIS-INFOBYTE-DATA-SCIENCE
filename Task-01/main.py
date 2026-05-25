import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv("menu.csv")

# Data cleaning
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
print(df.corr(numeric_only=True))

# Heatmap for correlation analysis
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("orrelation Heatmap")
plt.show()

# Distribution plot of Calories column
sns.histplot(df['Calories'], kde=True)
plt.title("Distribution of Calories")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.savefig("Distribution of calories")
plt.show()

# Average calories by category
df.groupby('Category')['Calories'].mean().plot(kind='bar')
plt.title("Average Calories by Category")
plt.xlabel("Food Category")
plt.ylabel("Average Calories")
plt.savefig("AVerage calories")
plt.show()


# Scatter plot between Total Fat and Calories
sns.scatterplot(x='Total Fat', y='Calories', data=df)
plt.title("Total Fat vs Calories")
plt.xlabel("Total Fat")
plt.ylabel("Calories")
plt.savefig("Fat vs calories")
plt.show()
