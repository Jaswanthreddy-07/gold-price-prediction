import pandas as pd

df = pd.read_csv("data/FINAL_USO.csv")

print("Original Shape:", df.shape)

df = df.drop_duplicates()

df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv("data/clean_gold.csv", index=False)

print("Cleaned dataset saved.")
