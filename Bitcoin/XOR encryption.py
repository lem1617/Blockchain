# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:23:13 2021

@author: Admin
"""
# XOR encryption
import binascii
from itertools import cycle 
 
key = "blockchain"
message1 = "This is such a great class"
message2 = "bitcoin"

### Using XOR encrypt
cipher_text1 = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(message1,cycle(K)))
print(cipher_text)
cipher_text2 = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(message2,cycle(K)))
print(cipher_text1)
print(cipher_text2)

### Convert cipher text into byte 
bytes_str = bytes(cipher_text1, 'utf-8')
rs1 = binascii.hexlify(bytes_str)
print(rs1)
bytes_str = bytes(cipher_text2, 'utf-8')
rs2 = binascii.hexlify(bytes_str)
print(rs2)

### Decode
plain_text1 = "".join(chr(ord(x) ^ ord(y)) for x,y in zip(cipher_text1, cycle(K)))
plain_text2 = "".join(chr(ord(x) ^ ord(y)) for x,y in zip(cipher_text2, cycle(K)))
print(plain_text1)
print(plain_text2)





	

