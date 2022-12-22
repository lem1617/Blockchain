# Function to generate new P2SH address

from bitcoinutils.setup import setup
from bitcoinutils.keys import P2shAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script

def p2sh_address():
    setup('testnet')
    
    # public key
    pub1 = '03ea03d0e44730a559148f4d3c986d31ee50383fc7e87ab3293c297ea70e825d76'
    pub2 = '03a683ed2b044c0a98c0f9e87f8e7640b033989ac79e6861ab2b4ddfff91831ba1'
   
    # create the redeem script
    redeem_script = Script([2, pub1, pub2, 2, 'OP_CHECKMULTISIG'])

    # generate P2SH address from the redeem script
    addr = P2shAddress.from_script(redeem_script)
    print('P2SH address: ', addr.to_string())

p2sh_address()
