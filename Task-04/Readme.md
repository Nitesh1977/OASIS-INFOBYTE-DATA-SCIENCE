# Twitter Data Cleaning 🐦

Hey! This is a simple Python project I built during my internship at **Oasis Infobyte**. It takes raw Twitter data and cleans it up so it's ready for sentiment analysis or any NLP task.

## What does it do?
Honestly, Twitter data is messy. Tweets have URLs, random symbols, numbers, and all sorts of noise. This script just fixes all of that:
- Loads the raw Twitter CSV file
- Drops any empty or duplicate rows
- Cleans the tweet text — removes links, special characters, and converts everything to lowercase
- Saves the cleaned version as a new CSV file
That's it. Simple and effective.

## Libraries Used
- `pandas` — for loading and handling the data
- `re` — for text cleaning using regular expressions (comes built-in with Python)

## How to Run
First, install the dependency:
```bash
pip install pandas
```
Then make sure `Twitter_Data.csv` is in the same folder as the script.
Now just run:
```bash
python main.py
```
You'll get a `cleaned_twitter_data.csv` file ready to use! ✅

## Project Files
| File | What it is |
|---|---|
| `main.py` | The main script |
| `Twitter_Data.csv` | Raw input data |
| `cleaned_twitter_data.csv` | Cleaned output data |
