# 📱 Google Play Store EDA & Sentiment Analysis
A data analysis project that explores Google Play Store app data and performs sentiment analysis on user reviews. Packed with visualizations to understand app trends, ratings, installs, and user opinions.

### Datasets
| File | Description |
|------|-------------|
| `apps.csv` | App details — category, installs, price, ratings, type |
| `user_reviews.csv` | User reviews with translated text for sentiment analysis |
## 🔍 What This Project Does

### 📊 Part 1 — App Data EDA (`apps.csv`)
1. Cleans messy data — removes `+`, `,`, `$` symbols and converts to numeric
2. Drops duplicates and null values
3. Generates these plots:
   - 🗂️ **App Categories Distribution** — which categories have the most apps
   - ⭐ **Ratings Distribution** — how ratings are spread across all apps
   - 📦 **Top Categories by Installs** — top 10 most installed categories
   - 💰 **Free vs Paid Apps** — how many apps are free vs paid
   - 🔥 **Correlation Heatmap** — relationships between numeric features
   - 🫧 **Interactive Scatter Plot** — Rating vs Reviews colored by Category (Plotly)

### 💬 Part 2 — Sentiment Analysis (`user_reviews.csv`)
1. Drops nulls and empty translated reviews
2. Uses **TextBlob** to calculate polarity of each review
3. Labels reviews as **Positive**, **Negative**, or **Neutral**
4. Plots a **Sentiment Distribution** bar chart

## 🚀 How to Run
bash
# 1. Clone the repo
git clone https://github.com/your-username/playstore-eda-sentiment.git
cd-playstore-eda-sentiment
# 2. Install dependencies
pip install pandas matplotlib seaborn plotly textblob
# 3. Run the script
python main.py

## 📦 Requirements
pandas
matplotlib
seaborn
plotly
textblob

## 🖼️ Output Plots

| File | Description |
|------|-------------|
| `App Categories Distribution.png` | Category-wise app count |
| `Ratings Distribution.png` | Histogram of app ratings |
| `Top Categories by Installs.png` | Top 10 categories by avg installs |
| `Free vs Paid Apps.png` | Free vs Paid app count |
| `Correlation Heatmap.png` | Numeric feature correlations |
| Interactive Plotly chart | Rating vs Reviews (opens in browser) |

## 🛠️ Tech Stack
- Python 3.x
- pandas, matplotlib, seaborn
- plotly (interactive charts)
- TextBlob (NLP sentiment analysis)

---

## 📁 Project Structure
playstore-eda-sentiment/
│
├── main.py                              # Main script
├── apps.csv                             # App dataset
├── user_reviews.csv                     # Reviews dataset
├── README.md                            # You're here!
└── *.png                                # Auto-generated plots

## 🙌 Contributing
Pull requests are welcome! Feel free to open an issue for bugs or new ideas.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
