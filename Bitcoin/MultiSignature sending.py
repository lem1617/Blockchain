from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script


def multiSig():
    setup('testnet')

    # create transaction input from tx id of MultiSig UTXO (contained 0.03276546 tBTC)
    input = TxInput('2406df580bc747a1962e37db825671309d99c44bf2e2c90ee58b1635746c651f', 0)
    
    # get public key
    pub1 = PublicKey('03ea03d0e44730a559148f4d3c986d31ee50383fc7e87ab3293c297ea70e825d76')
    public1 = pub1.to_hex(compressed=True)
    pub2 = PublicKey('02019662a808d4a0df7e8c1ee8b26646e59cfaa92ebd906bde14b4bda5113fa2a9')
    public2 = pub2.to_hex(compressed=True)
     
    output = TxOutput(to_satoshis(0.0042), Script([2, public1, public2, 2, 'OP_CHECKMULTISIG']))
    
    # create another output to get the change - remaining 0.00356546 is tx fees
    change_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42') 
    change_out = TxOutput(to_satoshis(0.025), Script(['OP_DUP', 'OP_HASH160', 
                                                        change_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))

    # create transaction from inputs/outputs -- default locktime is used
    tx = Transaction([input], [output, change_out])

    # use the private key corresponding to the address that contains the UTXO to sign the input
    priv = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1oq5z2AwwjzMWb3yhze5FQX')
    from_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42') 
    sig = priv.sign_input(tx, 0, Script(['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 
                                       'OP_EQUALVERIFY', 'OP_CHECKSIG']))
     
    # get public key as hex
    pub = priv.get_public_key().to_hex()

    # unlocking script
    input.script_sig = Script([sig, pub])
    signed_tx = tx.serialize()
    
    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)

multiSig()

# TxID: 28c8c16faabf14957438b165e2be5a4cc7af973b93ac3985828c99369272ce4d