import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv("data/raw/creditcard.csv")

# Reproducible randomness
np.random.seed(42)

# UPI Apps
apps = [
    "PhonePe",
    "Google Pay",
    "Paytm",
    "BHIM",
    "Amazon Pay"
]

# Cities
cities = [
    "Mumbai",
    "Pune",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai"
]

# Add UPI fields
df["Transaction_ID"] = [
    f"UPI{100000+i}"
    for i in range(len(df))
]

df["UPI_App"] = np.random.choice(
    apps,
    len(df)
)

df["City"] = np.random.choice(
    cities,
    len(df)
)

df["Hour"] = (
    df["Time"] // 3600
).astype(int) % 24

# Save processed dataset
import os

print("Current Working Directory:")
print(os.getcwd())

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/upi_transactions.csv",
    index=False
)

print("UPI Dataset Created Successfully!")
print(df.head())