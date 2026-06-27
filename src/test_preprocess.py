import pandas as pd
from preprocess import preprocess_data

# Load dataset
df = pd.read_csv("data/processed/upi_transactions_v2.csv")

# Take first 5 rows
df = df.head(5)

# Preprocess
processed_df = preprocess_data(df)

print("Original Shape:", df.shape)
print("Processed Shape:", processed_df.shape)