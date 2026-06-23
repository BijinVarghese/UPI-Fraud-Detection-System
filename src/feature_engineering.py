import pandas as pd
import numpy as np
import os

# Load transformed data
df = pd.read_csv("data/processed/upi_transactions.csv")

np.random.seed(42)

merchants = [
    "Swiggy",
    "Zomato",
    "Amazon",
    "Flipkart",
    "Myntra",
    "IRCTC",
    "BigBasket",
    "Blinkit"
]

df["Merchant"] = np.random.choice(
    merchants,
    len(df)
)

df["Device_ID"] = [
    f"DEV{100000+i}"
    for i in range(len(df))
]

df["Risk_Score"] = np.random.randint(
    1,
    101,
    len(df)
)

df["Night_Transaction"] = np.where(
    (df["Hour"] >= 0) & (df["Hour"] <= 5),
    1,
    0
)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/upi_transactions_v2.csv",
    index=False
)

print("Feature Engineering Completed!")
print(df.head())