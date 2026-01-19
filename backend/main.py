from flask import Flask, request, jsonify
from wallet import generate_wallet
from payment import process_payment
from withdrawal import withdraw_to_wallet
from database import init_db
import schedule
import time
import threading
from scripts.collect_profit import collect_profit

app = Flask(__name__)
init_db()

def hourly_profit_collection():
    while True:
        schedule.run_pending()
        time.sleep(60)

schedule.every().hour.do(lambda: collect_profit())
threading.Thread(target=hourly_profit_collection, daemon=True).start()

# Collect profits on startup
collect_profit()

@app.route('/generate', methods=['POST'])
def generate_wallet_endpoint():
    chain = request.json.get('chain', 'bitcoin')
    wallet = generate_wallet(chain)
    return jsonify(wallet)

@app.route('/pay', methods=['POST'])
def process_payment_endpoint():
    data = request.json
    result = process_payment(data['wallet_id'], data['amount'], data['currency'])
    return jsonify(result)

@app.route('/withdraw', methods=['POST'])
def withdraw_endpoint():
    result = withdraw_to_wallet(request.json)
    return jsonify(result)

@app.route('/collect-immediate', methods=['POST'])
def collect_immediate_endpoint():
    result = collect_profit()
    return jsonify({'success': True, 'amount': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
