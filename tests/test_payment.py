import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api.payment import process_payment

def test_process_payment():
    result = process_payment('test_wallet', 1000, 'INR')
    assert result['success'] is True
    assert 'tx_id' in result
    assert result['amount'] == 1000
    assert result['currency'] == 'INR'
