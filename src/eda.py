import pandas as pd

df = pd.read_csv("data/raw/creditcard.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFraud Distribution:")
print(df["Class"].value_counts())

print("\nFraud Percentage:")
fraud_percent = (df["Class"].sum() / len(df)) * 100
print(round(fraud_percent, 4), "%")

print("\nAmount Statistics:")
print(df["Amount"].describe())