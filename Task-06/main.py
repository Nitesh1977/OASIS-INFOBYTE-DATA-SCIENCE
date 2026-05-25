#  Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

# Data Loading and Exploring 
df = pd.read_csv("WineQT.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())

# CORRELATION HEATMAP
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("Correlation Heatmap.png")
plt.show()

# FEATURE / TARGET SPLIT
X = df.drop('quality', axis=1)
y = df['quality']

#  TRAIN / TEST SPLIT
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)  

# MODEL TRAINING — Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train, y_train)

# PREDICTION & EVALUATION
y_pred = model.predict(X_test)
print(y_pred)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)

# FEATURE IMPORTANCE PLOT
plt.figure(figsize=(8,5))
sns.barplot(x=model.feature_importances_, y=X.columns)
plt.title("Feature Importance")
plt.savefig("Importance of wine.png")
plt.show()

# SGD Classifier
from sklearn.linear_model import SGDClassifier
sgd_model = SGDClassifier()
sgd_model.fit(X_train, y_train)
sgd_pred = sgd_model.predict(X_test)
print(sgd_pred)
sgd_accuracy = accuracy_score(y_test, sgd_pred)
print("SGD Accuracy:", sgd_accuracy)

# SVC Classifier
from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(X_train, y_train)
svc_pred = svc_model.predict(X_test)
print(svc_pred)
svc_accuracy = accuracy_score(y_test, svc_pred)
print("SVC Accuracy:", svc_accuracy)