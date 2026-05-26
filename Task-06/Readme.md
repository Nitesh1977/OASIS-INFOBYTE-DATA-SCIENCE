# 🍷 Wine Quality Predictor

A machine learning project that predicts wine quality based on its chemical properties. Uses Random Forest, SGD, and SVC classifiers to find the best model.

## 📂 Dataset
- File: `WineQT.csv`
- Target column: `quality`
- All other columns are used as features

## 🔍 What This Project Does
1. **Loads & explores the data** — checks shape, nulls, and basic stats
2. **Plots a correlation heatmap** — saved as `Correlation Heatmap.png`
3. **Trains 3 ML models:**
   - 🌲 Random Forest Classifier
   - ⚡ SGD Classifier
   - 🔵 SVC (Support Vector Classifier)
4. **Evaluates each model** using accuracy score
5. **Shows feature importance** — saved as `Importance of wine.png`

## 🚀 How to Run
```bash
# 1. Clone the repo
git clone https://github.com/your-username/wine-quality-predictor.git
cd wine-quality-predictor

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# 3. Run the script
python wine_quality.py
```

## 📦 Requirements
```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 📊 Output
| Model | Metric |
|-------|--------|
| Random Forest | Accuracy score printed |
| SGD Classifier | Accuracy score printed |
| SVC | Accuracy score printed |

Two plots are saved automatically:
- `Correlation Heatmap.png`
- `Importance of wine.png`

## 🛠️ Tech Stack
- Python 3.x
- scikit-learn
- pandas & numpy
- matplotlib & seaborn

---

## 📁 Project Structure
```
wine-quality-predictor/
│
├── wine_quality.py        # Main script
├── WineQT.csv             # Dataset
├── README.md              # You're here!
└── outputs/
    ├── Correlation Heatmap.png
    └── Importance of wine.png
```
## 🙌 Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or want to suggest an improvement.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
