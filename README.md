# 🪙 Gold Price Prediction Using Machine Learning

A supervised machine learning project that predicts the gold price (closing price) from historical market data using a **Random Forest Regressor**. Built as a course-end project for B.Tech in Computer Science and Engineering (AI) at Chaitanya Bharathi Institute of Technology (2024-25).

## Overview

Gold prices are volatile and depend on many market factors. This project trains a Random Forest model on historical gold price data together with stock index, US Dollar Index and oil fund (USO) data, and evaluates it with MAE, RMSE and R² along with visual analysis (actual vs. predicted, residuals, feature importance).

## Project Structure

```
gold-prcie-predction/
├── app/       # Prediction application
├── data/      # Dataset (FINAL_USO.csv)
├── models/    # Trained model files
├── src/       # Training, evaluation and visualization code
└── README.md
```

## Dataset

- **File:** `FINAL_USO.csv` (daily historical data, merged on the `Date` column)
- **Sources cited in the report:** Yahoo Finance, Quandl
- **Target:** `Close` (gold closing price)
- **Features (9):**

| Feature | Description |
|---------|-------------|
| `Open`, `High`, `Low` | Daily price levels |
| `Adj Close` | Adjusted closing price |
| `Volume` | Trading volume |
| `SP_close` | S&P 500 close |
| `DJ_close` | Dow Jones close |
| `USDI_Price` | US Dollar Index price |
| `USO_Close` | United States Oil Fund close |

## Methodology

1. **Load and clean data:** parse dates, select features, drop missing values
2. **Train-test split:** 80% train / 20% test (`random_state=42`)
3. **Feature scaling:** `StandardScaler` (fit on train, applied to test)
4. **Model:** `RandomForestRegressor(n_estimators=100, random_state=42)`
5. **Evaluation:** MAE, RMSE, R² score
6. **Visualization:** actual vs. predicted prices, metrics bar chart, residual distribution, feature importance

## Results

| Metric | Score |
|--------|-------|
| MAE | 0.06 |
| RMSE | 0.19 |
| R² | 1.00 |

Residuals are tightly centered around zero. Feature importance is dominated by `Adj Close`, `High`, `Low` and `Open`.

> **Note:** The very high R² is largely because same-day price features (`Open`, `High`, `Low`, `Adj Close`) are very close to the target `Close`, and the split is random rather than chronological. This makes the task easier than forecasting a *future* price. See *Future Improvements*.

## Tech Stack

- Python
- pandas, NumPy
- scikit-learn
- matplotlib, seaborn

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Jaswanthreddy-07/gold-prcie-predction.git
cd gold-prcie-predction
```

### 2. Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3. Run
Run the training script from `src/` (update the dataset path to `data/FINAL_USO.csv` if needed):
```bash
python src/<script_name>.py
```

## Future Improvements

- Predict **future** prices using a chronological train-test split and lagged / moving-average features, without same-day price columns
- Hyperparameter tuning with `GridSearchCV` (`n_estimators`, `max_depth`, `min_samples_split`)
- Deep learning models (LSTM, GRU, Transformers) for time-series forecasting
- Ensemble models (XGBoost, LightGBM) and explainability with SHAP or LIME
- Live data via financial APIs and deployment as a web app on the cloud
- Sentiment analysis of financial news

## Disclaimer

This project is for educational purposes only and is not financial advice.

## Author

**Kasireddy Jaswanth Reddy**
B.Tech CSE (AI), Chaitanya Bharathi Institute of Technology, Proddatur
Guide: Dr. P. Pavankumar

[GitHub](https://github.com/Jaswanthreddy-07)
