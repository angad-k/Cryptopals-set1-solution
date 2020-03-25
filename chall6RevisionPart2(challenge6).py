import base64
from array import *
from binascii import unhexlify, b2a_hex

#XORs the two strings
def XORtwoSTRs(a, b):
    string3 = ""
    for i in range(0, len(a)):
        string3 += chr(ord(a[i])^ord(b[i]))
    return(string3)
#Scorer
def scorer(argument): 
    switcher = { 
        'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07,
        'e' : 12.0,
        't' : 9.10,
        'a' : 8.12,
        'o' : 7.68,
        'i' : 7.31,
        'n' : 6.95,
        's' : 6.28,
        'r' : 6.02,
        'h' : 5.92,
        'd' : 4.32,
        'l' : 3.98,
        'u' : 2.88,
        'c' : 2.71,
        'm' : 2.61,
        'f' : 2.30,
        'y' : 2.11,
        'w' : 2.09,
        'g' : 2.03,
        'p' : 1.82,
        'b' : 1.49,
        'v' : 1.11,
        'k' : 0.69,
        'x' : 0.17,
        'q' : 0.11,
        'j' : 0.10,
        'z' : 0.07,
    } 
    return int(switcher.get(argument, 0)) 


def switcher(argument): 
    switcher = { 
        # I iterated over the program a no. of times to get the perfect values to put here.
        # I knew key size is 29 from part1. 
        # Here, I tried taking the second best and in one case, third best scored String from the single byte XOR decryption to make the best fit.
        0 : 0,
        1 : 1,
        2 : 1,
        3 : 2,
        4 : 1,
        5 : 1,
        6 : 1,
        7 : 1,
        8 : 1,
        9 : 1,
        10 : 0,
        11 : 0,
        12 : 0,
        13 : 0,
        14 : 0,
        15 : 1,
        16 : 1,
        17 : 1,
        18 : 1,
        19 : 0,
        20 : 1,
        21 : 1,
        22 : 1,
        23 : 0,
        24 : 1,
        25 : 1,
        26 : 1,
        27 : 1,
        28 : 1,
        29 : 0,        
    } 
    return int(switcher.get(argument, 0)) 


def getBestXOR(stringA):
    maxval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bestStr = ["", "", "", "", "", "", "", "", "", "", ""]
    for i in range(32, 127):
        stringB = chr(i)*(len(stringA))
        result = (XORtwoSTRs(stringA,stringB))
        score = 0
        for j in range(0, len(result)):
            score += scorer(result[j]) 
        for j in range(0, len(maxval)):
            if(score > maxval[j]):
                tempScr = score
                tempStr = result
                for k in range(j, len(maxval)):
                    temp = maxval[k]
                    maxval[k] = tempScr
                    tempScr = temp
                    temp = bestStr[k]
                    bestStr[k] = tempStr
                    tempStr = temp
                break  
    return bestStr

def main():
    cipher = open('multiKEYencrypted.txt').read().splitlines()
    oneString = ""
    for line in cipher:
        line = base64.b64decode(line)
        oneString += line
    StrArray = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    i = 0
    while(i < len(oneString)):
        for j in range(0, 29):
            if((i+j) < len(oneString)):
                StrArray[j] += oneString[i + j]
        i = i + j + 1
    for i in range(0, 29):
        StrArray[i] = getBestXOR(StrArray[i])
    #After the above step, each element in StrArray is an Array in itself of all most probable strings.
    resultStr = ""
    for i in range(0, len(oneString)):
        for j in range(0, 29):
            x = switcher(j)
            if(i < len(StrArray)):
                resultStr += ((StrArray[j])[x])[i]
    print(resultStr)

if __name__== "__main__":
  main()