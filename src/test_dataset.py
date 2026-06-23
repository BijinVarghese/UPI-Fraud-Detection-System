import pandas as pd

df = pd.read_csv("data/raw/creditcard.csv")

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())
