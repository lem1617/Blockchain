from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script

def multisig():
    setup('testnet')

    # create transaction input from tx id of MultiSig UTXO (contained 0.00476483 tBTC)
    input = TxInput('28c8c16faabf14957438b165e2be5a4cc7af973b93ac3985828c99369272ce4d', 0)

    # Send 0.0042 tBTC and lock the script
    addr = P2pkhAddress('msfTfNj6FicTNBShCJBhoxvhHoM794cKsZ')
    output = TxOutput(to_satoshis(0.0042), Script(['OP_DUP', 'OP_HASH160', addr.to_hash160(), 
                                                  'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    
    # create transaction from inputs/outputs
    tx = Transaction([input], [output])

    # print raw transaction
    print("\nRaw unsigned transaction:\n" + tx.serialize())

    # use the private key corresponding to the address that contains the UTXO to unlock the input
    # Partner_1's private key
    priv1 = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1ojuat9jZouACYFT86628Lr') 
    
    # Partner_1's public key and Partner_2's public key locked in ScriptPubKey
    pub1 = PublicKey('03ea03d0e44730a559148f4d3c986d31ee50383fc7e87ab3293c297ea70e825d76')
    public1 = pub1.to_hex(compressed=True)
    pub2 = PublicKey('02019662a808d4a0df7e8c1ee8b26646e59cfaa92ebd906bde14b4bda5113fa2a9')
    public2 = pub2.to_hex(compressed=True)
    
    # Partner_1's signature
    sig1 = priv1.sign_input(tx, 0, Script([2, public1, public2, 2, 'OP_CHECKMULTISIG']))
    
    print("\n Partner_1's signature:\n" + sig1)
    
    # Partner_2's private key - to be filled in
    # priv2 = PrivateKey('') 
    
    # Partner_2's signature
    # sig2 = priv2.sign_input(tx, 0, Script([2, public1, public2, 2, 'OP_CHECKMULTISIG']))
    
    # set the scriptSig (unlocking script)
    # txin.script_sig = Script([0, sig1, sig2])
    # signed_tx = tx.serialize()
    
    # print raw signed transaction ready to be broadcasted
    # print("\nRaw signed transaction:\n" + signed_tx)

    # Result: raw unsigned transaction and signature of Partner_1
    
multisig()

## Raw unsigned transaction:
# 02000000014dce729236998c828539ac933b97afc74c5abee265b138749514bfaa6fc1c8280000000000ffffffff01a0680600000000001976a914853d5a191fd2ab19ebbd9519a696e5f30f7d119788ac00000000

## Partner_1's signature:
# 30450221009abd22af9f6e1a0d265146afc5f37f1aa863d3739c087cb10e0fef0a13745ade02204c5f7038999d80029f7fae88bf4fc8b794831565b793e0cd700f78b21f4cef7701