import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sql/upi_fraud.db")

queries = {

    "1. Total Transactions":
    "SELECT COUNT(*) AS Total_Transactions FROM transactions;",

    "2. Total Fraud Transactions":
    "SELECT COUNT(*) AS Fraud_Transactions FROM transactions WHERE Class=1;",

    "3. Total Genuine Transactions":
    "SELECT COUNT(*) AS Genuine_Transactions FROM transactions WHERE Class=0;",

    "4. Fraud Percentage":
    """
    SELECT
    ROUND(100.0*SUM(Class)/COUNT(*),2) AS Fraud_Percentage
    FROM transactions;
    """,

    "5. Average Transaction Amount":
    "SELECT ROUND(AVG(Amount),2) AS Avg_Amount FROM transactions;",

    "6. Maximum Transaction Amount":
    "SELECT MAX(Amount) AS Max_Amount FROM transactions;",

    "7. Minimum Transaction Amount":
    "SELECT MIN(Amount) AS Min_Amount FROM transactions;",

    "8. Top 5 Highest Transactions":
    """
    SELECT Transaction_ID, Amount
    FROM transactions
    ORDER BY Amount DESC
    LIMIT 5;
    """,

    "9. Fraud by City":
    """
    SELECT City, COUNT(*) AS Fraud_Count
    FROM transactions
    WHERE Class=1
    GROUP BY City
    ORDER BY Fraud_Count DESC;
    """,

    "10. Fraud by UPI App":
    """
    SELECT UPI_App, COUNT(*) AS Fraud_Count
    FROM transactions
    WHERE Class=1
    GROUP BY UPI_App
    ORDER BY Fraud_Count DESC;
    """,

    "11. Fraud by Merchant":
    """
    SELECT Merchant, COUNT(*) AS Fraud_Count
    FROM transactions
    WHERE Class=1
    GROUP BY Merchant
    ORDER BY Fraud_Count DESC;
    """,

    "12. Night Transactions":
    """
    SELECT COUNT(*) AS Night_Transactions
    FROM transactions
    WHERE Night_Transaction=1;
    """,

    "13. Night Fraud":
    """
    SELECT COUNT(*) AS Night_Fraud
    FROM transactions
    WHERE Night_Transaction=1
    AND Class=1;
    """,

    "14. Average Risk Score":
    """
    SELECT ROUND(AVG(Risk_Score),2)
    AS Average_Risk
    FROM transactions;
    """,

    "15. Highest Risk Score":
    """
    SELECT MAX(Risk_Score)
    AS Highest_Risk
    FROM transactions;
    """
}

for title, query in queries.items():

    print("\n")
    print("="*70)
    print(title)
    print("="*70)

    result = pd.read_sql(query, conn)

    print(result)

conn.close()