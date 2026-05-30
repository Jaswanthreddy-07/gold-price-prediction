import pandas as pd

df = pd.read_csv("data/clean_gold.csv")

# Moving Averages
df["Gold_7Day_Avg"] = df["Adj Close"].rolling(7).mean()

df["Gold_30Day_Avg"] = df["Adj Close"].rolling(30).mean()

# Lag Features
df["Lag_1"] = df["Adj Close"].shift(1)

df["Lag_7"] = df["Adj Close"].shift(7)

# Volatility
df["Volatility"] = (
    df["High"] - df["Low"]
)

df = df.dropna()

df.to_csv(
    "data/processed_gold.csv",
    index=False
)

print("Feature Engineering Complete")
