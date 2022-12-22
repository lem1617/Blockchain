from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script


def send_to_newp2sh():
    setup('testnet')

    # create transaction input from tx id of UTXO P2PKH (contained 0.00058 tBTC)
    input = TxInput('27142139e23a642f5eaeef215803c7848274a357c45b70feb5529c5a7b0e688a', 1)

    # output with non-standard script wrapped in P2SH, remaining 0.00035 is tx fees
    new_address = P2shAddress('2NEATeQ15bxsWsuEUpZXtQYxkzG4YZjQZju')
    output = TxOutput(to_satoshis(0.00023), Script(['OP_HASH160', 
                                                   new_address.to_hash160(), 'OP_EQUAL']) ) 

    # create transaction - default locktime is used
    tx = Transaction([input], [output])

    # keys and address corresponding to the UTXO
    priv = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1oq5z2AwwjzMWb3yhze5FQX')
    pub = priv.get_public_key().to_hex()
    from_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42')

    # signature for the txin
    sig = priv.sign_input(tx, 0, from_addr.to_script_pub_key() )

    # set the scriptSig (unlocking script)
    input.script_sig = Script([sig, pub])
    signed_tx = tx.serialize()

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)
    print("\nTxId:", tx.get_txid())

send_to_newp2sh()

# TxId: 1dd3045fc960ce8f37cfad86a976096a0e7dadd752d2ee5faca8f85f0e1c2680