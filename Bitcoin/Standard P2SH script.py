# function that sends some value to the previous P2SH address

from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script

def send_to_p2sh():
    setup('testnet')

    # create transaction input from tx id of UTXO (containing 0.001 tBTC)
    input = TxInput('893e0cb8ce067f5ee92aa526f5e98b1230ee193a8c2f58ac9b4584decace4972', 1)
    
    # create transaction
    p2sh_address = P2shAddress('2NCb32ayrt3ciASpXQukb94pQbRKtdRpVar')
    output = TxOutput(to_satoshis(0.00032), Script(['OP_HASH160', p2sh_address.to_hash160(), 'OP_EQUAL']) )

    # change output to P2PKH address - remaining 0.0001 is tx fees
    change_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42')
    change_output = TxOutput(to_satoshis(0.00058), change_addr.to_script_pub_key())
    
    # create transaction - default locktime is used
    tx = Transaction([input], [output, change_output])

    # keys and address corresponding to the UTXO
    priv = PrivateKey('cMahea7zqjxrtgAbB7LSGbcQUr1uX1oq5z2AwwjzMWb3yhze5FQX')
    pub = priv.get_public_key().to_hex()
    from_addr = P2pkhAddress('mr92LX6JSCD9Yghje1cZyuJxDBv6adLq42')
    
    # signature 
    sig = priv.sign_input(tx, 0, from_addr.to_script_pub_key() )

    # set the scriptSig (unlocking script)
    input.script_sig = Script([sig, pub])
    signed_tx = tx.serialize()

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)
    print("\nTxId:", tx.get_txid())

send_to_p2sh()

## TxId: 27142139e23a642f5eaeef215803c7848274a357c45b70feb5529c5a7b0e688a