import os
import hashlib
import base58check
import eth_keys
from solana.keypair import Keypair

def generate_bitcoin_wallet():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(bytes.fromhex(private_key)).hexdigest()
    address = base58check.b58encode_check(
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
    keypair = Keypair.generate()
    private_key = keypair.secret_key.hex()
    public_key = keypair.public_key.hex()
    address = keypair.public_key.to_string()
    
    return {
        'private_key': private_key,
        'public_key': public_key,
        'address': address
    }
