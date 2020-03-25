from binascii import unhexlify, b2a_hex
import base64
import array as arr


def XORtwoSTRs(a, b):
    string1 = unhexlify(a)
    string2 = unhexlify(b)
    string3 = ""
    for i in range(0, len(string1)):
        string3 += chr(ord(string1[i])^ord(string2[i]))
    return(string3)

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

def checkXOR(stringA):
    maxval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(32, 127):
        stringB = hex(i)[2:]*(len(stringA)/2)
        result = (XORtwoSTRs(stringA,stringB))
        score = 0
        for j in range(0, len(result)):
            score += scorer(result[j]) 
        for j in range(0, len(maxval)):
            if(score > maxval[j]):
                tempScr = score
                for k in range(j, len(maxval)):
                    temp = maxval[k]
                    maxval[k] = tempScr
                    tempScr = temp
                break
    resultscore = maxval[0] + maxval[1] + maxval[2] + maxval[3] + maxval[4] + maxval[5] + maxval[6] + maxval[7] + maxval[8] + maxval[9]
    return resultscore


def main():
    maxval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bestStr = ["", "", "", "", "", "", "", "", "", "", ""]
    ciphers = open('chall3.txt').read().splitlines()
    for a in ciphers:
        score = checkXOR(a)
        for i in range(0, len(maxval)):
            if(score > maxval[i]):
                tempScr = score
                tempStr = a
                for j in range(i, len(maxval)):
                    temp = maxval[j]
                    maxval[j] = tempScr
                    tempScr = temp
                    temp = bestStr[j]
                    bestStr[j] = tempStr
                    tempStr = temp
                break
    print("The most probable strings are :")
    for i in bestStr :
        print(i)
        
if __name__== "__main__":
  main()

        
