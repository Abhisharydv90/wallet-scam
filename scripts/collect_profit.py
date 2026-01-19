import sqlite3
import time
import uuid

def collect_profit():
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM profits')
    profits = cursor.fetchall()
    total = sum(p[3] for p in profits)
    
    if total > 0:
        tx_hash = f"tx_{uuid.uuid4()}"
        print(f"Instant profit collected: ₹{total:,} (tx: {tx_hash})")
    
    conn.close()
    return total
