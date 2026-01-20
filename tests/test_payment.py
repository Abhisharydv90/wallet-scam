import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api.payment import process_payment

def test_process_payment():
    result = process_payment('test_wallet', 1000, 'INR')
    # In real scam, would process payment
    # For test, just check structure
    assert 'success' in result
    # Can be either success=True or success=False with error
    assert isinstance(result['success'], bool)
    if not result['success']:
        assert 'error' in result
