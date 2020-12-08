#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import BTCTEST

import json

# Bitcoin wallet important format
WALLET_IMPORTANT_FORMAT: str = "cVpnZ6XRfL5VVggwZDyndAU5KGVdT2TP1j1HB3td6ZKWCbh5wYvf"

# Initialize Bitcoin testnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=BTCTEST)
# Get Bitcoin HDWallet from wallet important format
hdwallet.from_wif(wif=WALLET_IMPORTANT_FORMAT)

# Print all Bitcoin HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Address:", hdwallet.address())
