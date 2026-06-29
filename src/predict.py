import joblib
import pandas as pd

# ==========================
# Load Model
# ==========================
model = joblib.load("models/random_forest_model.pkl")

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("data/processed/upi_transactions_v2.csv")

# Take one random transaction
sample = df.sample(1, random_state=42)

actual = sample["Class"].values[0]

# Remove unwanted columns
sample = sample.drop(
    columns=[
        "Class",
        "Transaction_ID",
        "Device_ID"
    ]
)

# One-hot encoding
sample = pd.get_dummies(
    sample,
    columns=[
        "UPI_App",
        "City",
        "Merchant"
    ]
)

# Load feature names
feature_names = joblib.load("models/feature_names.pkl")

# Add missing columns
for col in feature_names:
    if col not in sample.columns:
        sample[col] = 0

# Keep only training columns
sample = sample[feature_names]

# Prediction
prediction = model.predict(sample)[0]

print("="*50)
print("UPI FRAUD DETECTION")
print("="*50)

print("Actual Class :", actual)

if prediction == 1:
    print("Prediction   : FRAUD")
else:
    print("Prediction   : NORMAL")