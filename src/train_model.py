import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)
from imblearn.over_sampling import SMOTE

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("data/processed/upi_transactions_v2.csv")

# Use a smaller sample for faster training
df = df.sample(50000, random_state=42)

# ==========================
# Features and Target
# ==========================
# ==========================
# Features and Target
# ==========================
X = df.drop(
    columns=[
        "Class",
        "Transaction_ID",
        "Device_ID"
    ]
)

# Convert categorical columns into numbers
X = pd.get_dummies(
    X,
    columns=[
        "UPI_App",
        "City",
        "Merchant"
    ]
)

# Save feature names
feature_names = X.columns.tolist()

y = df["Class"]

# ==========================
# Split Data
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================
# Handle Class Imbalance
# ==========================
smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter SMOTE:")
print(y_train.value_counts())

# ==========================
# Train Model
# ==========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)
# Create models folder if it doesn't exist
# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model and feature names
joblib.dump(model, "models/random_forest_model.pkl")
joblib.dump(feature_names, "models/feature_names.pkl")

print("\nModel saved successfully!")
# ==========================
# Prediction
# ==========================
y_pred = model.predict(X_test)

# ==========================
# Evaluation
# ==========================
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))