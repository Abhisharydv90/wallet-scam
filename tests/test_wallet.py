import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api.wallet import generate_bitcoin_wallet

def test_generate_bitcoin_wallet():
    wallet = generate_bitcoin_wallet()
    assert 'private_key' in wallet
    assert 'public_key' in wallet
    assert 'address' in wallet
    assert len(wallet['private_key']) == 64
    assert len(wallet['public_key']) == 64
    assert wallet['address'].startswith('1') or wallet['address'].startswith('3')
