# 💳 Credit Card Fraud Detection
A machine learning project that detects fraudulent credit card transactions using multiple classifiers and anomaly detection. Built to handle real-world imbalanced data.

## 📂 Dataset
- File: `creditcard.csv`
- Target column: `Class` (0 = Normal, 1 = Fraud)
- `Time` and `Amount` columns are preprocessed before training

## 🔍 What This Project Does
1. **Loads & explores the data** — checks info, nulls, and class distribution
2. **Plots fraud vs normal transactions** — saved as `Fraud_Distribution.png`
3. **Feature Engineering** — scales `Amount` using StandardScaler, drops `Time` & `Amount`
4. **Anomaly Detection** — uses Isolation Forest to catch unusual transactions
5. **Trains 3 ML Models:**
   - 📈 Logistic Regression
   - 🌿 Decision Tree Classifier
   - 🌲 Random Forest Classifier
6. **Evaluates each model** using ROC-AUC score & classification report
7. **Real-time simulation** — uses the best model (Random Forest) to flag the first 10 test transactions as 🚨 FRAUD or ✅ Normal

## 🚀 How to Run
# 1. Clone the repo
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
# 2. Install dependencies
pip install pandas scikit-learn matplotlib seaborn
# 3. Run the script
python main.py

## 📦 Requirements
pandas
scikit-learn
matplotlib
seaborn

## 📊 Output
| Model | Metric |
|-------|--------|
| Logistic Regression | ROC-AUC + Classification Report |
| Decision Tree | ROC-AUC + Classification Report |
| Random Forest | ROC-AUC + Classification Report |
| Isolation Forest | Classification Report (Anomaly Detection) |

Plot saved automatically:
`Fraud_Distribution.png`

## 🛠️ Tech Stack
- Python 3.x
- scikit-learn
- pandas
- matplotlib & seaborn

## 📁 Project Structure
credit-card-fraud-detection/
│
├── main.py                    # Main script
├── creditcard.csv             # Dataset
├── README.md                  # You're here!
└── Fraud_Distribution.png     # Auto-generated plot

## 🙌 Contributing
Pull requests are welcome! Feel free to open an issue for bugs or feature suggestions.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).Task-07
