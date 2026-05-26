import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# DATA LOADING & EDA
df = pd.read_csv("creditcard.csv")
print(df.head(), df.info(), df.isnull().sum())
print("Class Distribution:\n", df['Class'].value_counts())

# ── 2. FRAUD DISTRIBUTION PLOT 
sns.countplot(x='Class', data=df)
plt.title("Fraud vs Normal Transactions")
plt.savefig("Fraud_Distribution.png")
plt.show()

# FEATURE ENGINEERING 
df['Amount_Scaled'] = StandardScaler().fit_transform(df[['Amount']])
df.drop(columns=['Time', 'Amount'], inplace=True)

X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ANOMALY DETECTION 
iso = IsolationForest(contamination=0.002, random_state=42)
iso_pred = [1 if p == -1 else 0 for p in iso.fit_predict(X_test)]
print("\nIsolation Forest:\n", classification_report(y_test, iso_pred))

# ── 5. ML MODELS 
models = {
    "Logistic Regression" : LogisticRegression(max_iter=1000, class_weight='balanced'),
    "Decision Tree"       : DecisionTreeClassifier(class_weight='balanced'),
    "Random Forest"       : RandomForestClassifier(n_estimators=100, class_weight='balanced'),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"\n{name}  |  ROC-AUC: {roc_auc_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred))

# REAL-TIME MONITORING SIMULATION
best = models["Random Forest"]
for i, p in enumerate(best.predict(X_test[:10])):
    print(f"Transaction {i+1}: {'🚨 FRAUD' if p==1 else '✅ Normal'}")