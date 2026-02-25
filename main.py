from src.fraud_detection import FraudDetector
from src.blockchain_verifier import BlockchainVerifier
from src.dashboard_app import DashboardApp
from src.alerts import send_alert

# Step 1: Detect Fraud
detector = FraudDetector()
df = detector.load_data('data/supply_chain_sample.csv')
df = detector.detect_fraud()
fraudulent_transactions = detector.get_fraudulent_transactions()

# Step 2: Send Alerts
send_alert(fraudulent_transactions)

# Step 3: Verify transactions via Blockchain
verifier = BlockchainVerifier()
for _, tx in df.iterrows():
    verifier.add_transaction(tx.to_dict())

# Verify a sample transaction
sample_tx = df.iloc[0].to_dict()
is_verified = verifier.verify_transaction(sample_tx)
print(f"\nTransaction verification for TXID {sample_tx['transaction_id']}: {is_verified}")

# Step 4: Launch Dashboard
dashboard = DashboardApp(df)
dashboard.run()
