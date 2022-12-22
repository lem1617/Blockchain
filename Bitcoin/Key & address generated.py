# Generate new public key, private key & address

from bitcoinutils.setup import setup
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey

def main():
    # always remember to setup the network
    setup('mainnet')

    # create a private key (deterministically)
    priv = PrivateKey(secret_exponent = 1)

    # compressed is the default
    print("\nPrivate key WIF:", priv.to_wif(compressed=True))

    # could also instantiate from existing WIF key
    #priv = PrivateKey.from_wif('KwDiBf89qGgbjEhKnhxjUh7LrciVRzI3qYjgd9m7Rfu73SvHnOwn')

    # get the public key
    pub = priv.get_public_key()

    # compressed is the default
    print("Public key:", pub.to_hex(compressed=True))

    # get address from public key
    address = pub.get_address()

    # print the address and hash160 - default is compressed address
    print("Address:", address.to_string())
    print("Hash160:", address.to_hash160())

    print("\n--------------------------------------\n")


if __name__ == "__main__":
    main()