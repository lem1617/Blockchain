from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from bitcoinutils.script import Script

def send_p2phk():
    # setup the network
    setup('testnet')

    # create transaction input from tx id of UTXO (contained 0.01271558 tBTC)
    # specify the tx id and the index of the input you are using 
    txin = TxInput('4c8451baee33e405d4ffab8d2113ecaacde66d2055f1c92d6a117c9d9ba69393', 0)

    # create transaction output using P2PKH scriptPubKey (locking script)
    addr = P2pkhAddress('mreLpAzPWBtdwBC9NMEsBy1jkQ3phjy1Eh')
    txout = TxOutput(to_satoshis(0.0055), Script(['OP_DUP', 'OP_HASH160', addr.to_hash160(),
                                  'OP_EQUALVERIFY', 'OP_CHECKSIG']))
   
    # create transaction from inputs/outputs -- default locktime is used
    tx = Transaction([txin], [txout])
    
    # print raw transaction
    print("\nRaw unsigned transaction:\n" + tx.serialize())

    # use the private key corresponding to the address that contains the UTXO to sign the input
    sk = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1oq5z2AwwjzMWb3yhze5FQX') 
    
    # from address corresponding to the input
    from_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42') 
    sig = sk.sign_input(tx, 0, Script(['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 
                                       'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    
    # get public key as hex
    pk = sk.get_public_key().to_hex()

    # set the scriptSig (unlocking script)
    txin.script_sig = Script([sig, pk])
    signed_tx = tx.serialize()
    
    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)

send_p2phk()

# Transaction ID: aaa771cf51ee833daf1370a8de996a47c7e802b10fd8e70074934f5d6287f1b4
