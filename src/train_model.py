import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

df = pd.read_csv(
    "data/processed_gold.csv"
)

features = [
    'Open',
    'High',
    'Low',
    'SP_close',
    'DJ_close',
    'OF_Price',
    'OS_Price',
    'USDI_Price',
    'Gold_7Day_Avg',
    'Gold_30Day_Avg',
    'Lag_1',
    'Lag_7',
    'Volatility'
]

X = df[features]

y = df["Adj Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(
    "R2 Score:",
    r2_score(y_test, pred)
)

joblib.dump(
    model,
    "models/gold_model.pkl"
)

print("Model Saved")
