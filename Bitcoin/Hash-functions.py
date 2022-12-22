# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:50:59 2021

@author: Admin
"""
# Sending proof-of-work with hashing algorithm (SHA256)

import hashlib
import time
from itertools import count

def countZeros(x):
    #Allocate the size, we use SHA256 so the total bits is 256
    total_bits = 256
    
    result = 0
    #Count numbers of zero by shifting to the right until we meet 1
    while ((x & (1 << (total_bits - 1))) == 0):
        x = (x << 1)
        result += 1

    return result

#Start the timer
start = time.time()

#Loop until we get the desire result
for i in count(0):
    #Create and hash the string
    string_to_hash = "phan_dieu_linh:“DigitalEconomics”:" + str(i)
    hash_object = hashlib.sha256(str(string_to_hash).encode('utf-8'))
    hash = int(hash_object.hexdigest(), 16)

    #If the string meet the condition, print the time we find the proof of work, end 
    if countZeros(hash) == 25:
        print ('Proof of work 5: ', time.time() - start)
        break

# It takes 0.0s to find a proof-of-wook for 5 leading zeros
# It takes 0.0030629634857177734s to find a proof-of-wook for 10 leading zeros
# It takes 0.7844564914703369s to find a proof-of-wook for 20 leading zeros
# It takes 40.227065086364746s to find a proof-of-wook for 25 leading zeros
# It takes 2321.5561344623566s to find a proof-of-wook for 30 leading zeros

