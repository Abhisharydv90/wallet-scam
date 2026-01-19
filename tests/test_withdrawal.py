import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api.withdrawal import withdraw_to_wallet

def test_withdraw_to_wallet():
    result = withdraw_to_wallet('test_wallet', 1000)
    assert result['success'] is True
    assert 'tx_hash' in result
    assert result['amount'] == 1000
