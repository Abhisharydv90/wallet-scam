import sqlite3
import time

def init_db():
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wallets (
            id TEXT PRIMARY KEY,
            private_key TEXT,
            public_key TEXT,
            address TEXT,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            wallet_id TEXT,
            amount REAL,
            currency TEXT,
            tx_id TEXT,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS withdrawals (
            id TEXT PRIMARY KEY,
            wallet_id TEXT,
            amount REAL,
            address TEXT,
            tx_hash TEXT,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profits (
            id TEXT PRIMARY KEY,
            wallet_id TEXT,
            amount REAL,
            created_at TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
