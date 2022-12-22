from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script

def output_to_p2pkh():
    setup('testnet')

    # create transaction input from tx id of UTXO (contained 0.00023 tBTC)
    input = TxInput('1dd3045fc960ce8f37cfad86a976096a0e7dadd752d2ee5faca8f85f0e1c2680', 0) 

    # create tx output to P2PKH address - remaining 0.00003 tBTC is tx fee
    to_addr = P2pkhAddress('mgkswn7UohYskb8bED9BiQXMC5gMCjSoG3')
    output = TxOutput(to_satoshis(0.0002), to_addr.to_script_pub_key() )

    # create transaction - default locktime is used
    tx = Transaction([input], [output])

    # unlocking the input
    # private key 
    priv = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1oq5z2AwwjzMWb3yhze5FQX')
    # public key
    pub = priv.get_public_key().to_hex()

    # create the redeem script - needed to sign the transaction
    redeem_script = Script(['OP_ADD', 'OP_3', 'OP_EQUALVERIFY', pub, 'OP_CHECKSIG'])

    # signature for the txin
    sig = priv.sign_input(tx, 0, redeem_script )

    # set the scriptSig (unlocking script)
    input.script_sig = Script([sig, 'OP_1', 'OP_2', redeem_script.to_hex()])
    signed_tx = tx.serialize()

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)
    print("\nTxId:", tx.get_txid())

output_to_p2pkh()

# TxId: 73fd133ece6f9dfdf982fa2bb69895d3305fb6fb9af799e5a2270ce6d39634f7