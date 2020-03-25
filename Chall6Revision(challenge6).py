import base64
from binascii import unhexlify, b2a_hex

##tobits is copied from stack overflow
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

#returns HammingDistance
def hammingDistance(a, b):
    ba = tobits(a.encode('utf-8'))
    ba2 = tobits(b.encode('utf-8'))
    dist = 0
    for i in range(0, len(ba)):
        dist += ba[i]^ba2[i]
    return dist

#Prints the best key sizes
def getKeySize():
    cipher = open('multiKEYencrypted.txt').read().splitlines()
    oneString = ""
    for line in cipher:
        line = base64.b64decode(line)
        oneString += line
    arrayDist = []
    indArray = []
    for i in range(1, 50):
        a = ""
        b = ""
        for j in range(0, i):
            a += oneString[j]
            b += oneString[i+j]
        dist1 = float(hammingDistance(a, b))/float(i)
        a = ""
        b = ""
        for j in range(i, i+i):
            a += oneString[j]
            b += oneString[i+j]
        dist2 = float(hammingDistance(a, b))/float(i)
        avgDist = (dist1 + dist2)/2
        arrayDist.append(avgDist)
        indArray.append(i)
    print(indArray)
    print(arrayDist)
    for i in range(0, 48):
        for j in range(0, i):
            if(arrayDist[indArray[j] - 1] > arrayDist[indArray[j + 1] - 1] ):
                temp = indArray[j]
                indArray[j]= indArray[j + 1]
                indArray[j + 1] = temp
    for i in range(0, 10):
        print( "Keysize = " + str(indArray[i]) + " \t HammingDistance = " + str(arrayDist[indArray[i] - 1]))

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
    return switcher.get(argument, 0)

#this will brute force a single-byte XOR and return what seems the best.
def getBestXOR(stringA):
    maxval = 0
    bestStr = ""
    for i in range(32, 127):
        stringB = chr(i)*(len(stringA))
        result = (XORtwoSTRs(stringA,stringB))
        score = 0
        for j in range(0, len(result)):
            score += scorer(result[j]) 
        print(result)
        print(score)
        if(score > maxval):
            bestStr = result
            maxval = score
    return bestStr

def main():
    getKeySize()
    input()
    #next code is written after getting the possible keysizes.
    keyArr = [2, 5, 3, 18, 20, 8, 29] 
    cipher = open('multiKEYencrypted.txt').read().splitlines()
    oneString = ""
    for line in cipher:
        line = base64.b64decode(line)
        oneString += line
    
    for key in keyArr:
        StrArray = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        i = 0
        while (i < len(oneString)):
            for j in range(0, key):
                if((i + j) < len(oneString)):
                    StrArray[j] += oneString[i+j]
            i = i+j+1
        for i in range(0, key):
            StrArray[i]  = getBestXOR(StrArray[i])
        resultStr = ""

        for i in range(0, len(oneString)):
            for j in range(0, key):
                if(i < len(StrArray[j])):
                    resultStr += (StrArray[j])[i]
        print(resultStr)
        f= open("bestStrR" + str(key) + ".txt","w+")
        f.write(resultStr)

if __name__== "__main__":
  main()