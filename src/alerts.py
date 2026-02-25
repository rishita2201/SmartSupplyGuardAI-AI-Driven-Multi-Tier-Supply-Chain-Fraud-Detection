def send_alert(fraudulent_df):
    if fraudulent_df.empty:
        print("No fraud detected!")
        return
    print("⚠️ Fraud Alert! Suspicious Transactions Detected:")
    for _, row in fraudulent_df.iterrows():
        print(f"Transaction ID: {row['transaction_id']}, Supplier: {row['supplier_id']}, Product: {row['product_id']}, Amount: {row['total_value']}")
