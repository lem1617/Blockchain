# Blockchain
This repository contains Solidity, Blockchain, and Bitcoin Transaction and the Scripting language written on Python and Ethereum Smart Contract

## Bitcoin Scripting
Including python file to:
- *Generate keys and addresses*: P2PKH, P2SH, non-standard address, P2SH(P2WPKH).
- *Create transactions*: Send bitcoin and spend an output with different scripts: P2PKH, P2SH, MultiSignature, non-standard transactions.

## Ethereum smart contracts in Solidity
- *Simple Faucet*: Anyone can pay the contract to increase the contract's balance. Anyone can withdraw from the contract with a max amount being a variable that you specify.
- *Augmented Faucet*: Add max number of users to withdraw, specify the contract owner, function to reset the user list to allow new users to withdraw.
- *Blind Vickrey Auction*: Main properties include: Only a number of users can participate; Only owner can call the winner, when max_users have bid; The highest bidder wins the auction but pays the second best price; The winner get marked as "winner" inside the smart contract and everyone can see it; The losers must be reimbursed; The contract owner can reset everything and open the same contract again for another auction; and so on.
### Library:
https://github.com/karask/python-bitcoin-utils
