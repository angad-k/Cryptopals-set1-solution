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

def main():
    stringA = raw_input()
    maxval = 0
    bestStr = ""
    maxval2 = 0
    bestStr2 = ""
    maxval3 = 0
    bestStr3 = ""
    maxval4 = 0
    bestStr4 = ""
    maxval5 = 0
    bestStr5 = ""
    maxval6 = 0
    bestStr6 = ""
    maxval7 = 0
    bestStr7 = ""
    maxval8 = 0
    bestStr8 = ""
    maxval9 = 0
    bestStr9 = ""
    maxval10 = 0
    bestStr10 = ""
    maxval11 = 0
    bestStr11 = ""
    for i in range(32, 127):
        stringB = hex(i)[2:]*(len(stringA)/2)
        result = (XORtwoSTRs(stringA,stringB))
        score = 0
        for j in range(0, len(result)):
            score += scorer(result[j]) 
        print(result)
        print(score)
        #This if-else tree doesn't describe me as a person.
        if(score > maxval):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = bestStr5
            bestStr5 = bestStr4
            bestStr4 = bestStr3
            bestStr3 = bestStr2
            bestStr2 = bestStr
            bestStr = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = maxval5
            maxval5 = maxval4
            maxval4 = maxval3
            maxval3 = maxval2
            maxval2 = maxval
            maxval = score
        elif(score>maxval2):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = bestStr5
            bestStr5 = bestStr4
            bestStr4 = bestStr3
            bestStr3 = bestStr2
            bestStr2 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = maxval5
            maxval5 = maxval4
            maxval4 = maxval3
            maxval3 = maxval2
            maxval2 = score
        elif(score>maxval3):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = bestStr5
            bestStr5 = bestStr4
            bestStr4 = bestStr3
            bestStr3 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = maxval5
            maxval5 = maxval4
            maxval4 = maxval3
            maxval3 = score
        elif(score>maxval4):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = bestStr5
            bestStr5 = bestStr4
            bestStr4 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = maxval5
            maxval5 = maxval4
            maxval4 = score
        elif(score>maxval5):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = bestStr5
            bestStr5 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = maxval5
            maxval5 = score
        elif(score>maxval6):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = bestStr6
            bestStr6 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = maxval6
            maxval6 = score
        elif(score>maxval7):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = bestStr7
            bestStr7 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = maxval7
            maxval7 = score
        elif(score>maxval8):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = bestStr8
            bestStr8 = result
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = maxval8
            maxval8 = score   
        elif(score>maxval9):
            bestStr11 = bestStr10
            bestStr10 = bestStr9
            bestStr9 = result   
            maxval11 = maxval10
            maxval10 = maxval9
            maxval9 = score
        elif(score>maxval10):
            bestStr11 = bestStr10
            bestStr10 = result 
            maxval11 = maxval10
            maxval10 = score
        elif(score>maxval11):
            bestStr11 = result
            maxval11 = score
    print(bestStr)
    print(bestStr2)
    print(bestStr3)
    print(bestStr4)
    print(bestStr5)
    print(bestStr6)
    print(bestStr7)
    print(bestStr8)
    print(bestStr9)
    print(bestStr10)
    print(bestStr11)
if __name__== "__main__":
  main()



        
