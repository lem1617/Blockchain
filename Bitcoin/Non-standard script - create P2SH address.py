# Write a script that requires both a signature and a password to unlock
# create a P2SH address from this script

from bitcoinutils.setup import setup
from bitcoinutils.keys import P2shAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script

def newp2sh_address():
    setup('testnet')
    
    # public key
    pub = '03ea03d0e44730a559148f4d3c986d31ee50383fc7e87ab3293c297ea70e825d76'
    
    # create the redeem script contains a public key and password
    redeem_script = Script(['OP_ADD', 'OP_3', 'OP_EQUALVERIFY', pub, 'OP_CHECKSIG'])

    # generate P2SH address
    addr = P2shAddress.from_script(redeem_script)
    print('New P2SH address: ', addr.to_string())
    
newp2sh_address()
