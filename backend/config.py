import os

# Payment configuration
BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY', 'your_api_key')
BINANCE_SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY', 'your_secret_key')
WALLET_ADDRESS = os.environ.get('WALLET_ADDRESS', 'your_wallet_address')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///wallets.db')

# Scam configuration
WALLET_GENERATION_RATE = int(os.environ.get('WALLET_GENERATION_RATE', '1'))
PAYMENT_AMOUNT = float(os.environ.get('PAYMENT_AMOUNT', '1000'))
