from Crypto.Cipher import AES
import base64
from binascii import unhexlify, b2a_hex
#Took the help of internet for the logic of this one. 
cipher = open('AESc8.txt').read().splitlines()
bestStr = ["", "", "", "", "", "", ""]
scores = [0, 0, 0, 0, 0, 0]
bestScore = 0
bestStr = ""
for line in cipher:
    lineOg = line
    line = unhexlify(line)
    line =[ord(x) for x in line]
    arr = []
    k = 0
    a = ""
    for i in line:
        a += str(i)
        k = k + 1
        if(k==16):
            arr.append(a)
            a = ""
            k = 0
    score = len(arr) - len(set(arr))
    if(score>bestScore):
        score = bestScore
        bestStr = line
        bestStrOg = lineOg
print(bestStr) 
print(bestStrOg)
    
