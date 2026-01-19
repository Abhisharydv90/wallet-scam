import os
import hashlib
import base58
import eth_keys

def generate_bitcoin_wallet():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(bytes.fromhex(private_key)).hexdigest()
    address = base58.b58encode_check(
        b'\x00' + bytes.fromhex(public_key[:64])
    ).decode('utf-8')
    
    return {
        'private_key': private_key,
        'public_key': public_key,
        'address': address
    }

def generate_ethereum_wallet():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha3_256(bytes.fromhex(private_key)).hexdigest()
    address = '0x' + public_key[24:]
    
    return {
        'private_key': private_key,
        'public_key': public_key,
        'address': address
    }

def generate_solana_wallet():
    # Simplified to avoid Solana dependency
    private_key = os.urandom(32).hex()
    public_key = os.urandom(32).hex()
    address = "SOLANA_" + os.urandom(32).hex()[:32]
    
    return {
        'private_key': private_key,
        'public_key': public_key,
        'address': address
    }
