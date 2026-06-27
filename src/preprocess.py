import pandas as pd

def preprocess_data(df):
    """
    Preprocess transaction data for model prediction.
    """

    # Remove columns not used for training
    columns_to_drop = ["Class", "Transaction_ID", "Device_ID"]

    existing_columns = [col for col in columns_to_drop if col in df.columns]

    df = df.drop(columns=existing_columns)

    # Convert categorical columns into dummy variables
    categorical_columns = ["UPI_App", "City", "Merchant"]

    existing_categorical = [
        col for col in categorical_columns if col in df.columns
    ]

    df = pd.get_dummies(
        df,
        columns=existing_categorical
    )

    return df