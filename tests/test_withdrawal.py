import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api.withdrawal import withdraw_to_wallet

def test_withdraw_to_wallet():
    result = withdraw_to_wallet('test_wallet', 1000)
    # In real scam, would process withdrawal
    # For test, just check structure
    assert 'success' in result
    # Can be either success=True or success=False with error
    assert isinstance(result['success'], bool)
    if not result['success']:
        assert 'error' in result
