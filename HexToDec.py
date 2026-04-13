# --conding:utf-8--
import os
import regex
import math

nDecNum = 0
nHexPower = 1
MAX_INT = 2 ** 32 - 1
nMaxHexLen = math.ceil(math.log(MAX_INT, 16))
os.system("cls")
print("Input a hexadecimal number:")
strLine = input()
nStrLen = len(strLine)
oMatches = regex.fullmatch("^[0-9A-Fa-f]+$", strLine)
bRightString = (nStrLen <= nMaxHexLen and oMatches is not None)
if (not bRightString):
    print("Wrong hexadecimal number format!!!")
    exit(0)
for i in range(nStrLen):
    nHexDigit = 0
    chHexDigit = strLine[nStrLen - 1 - i]
    if (chHexDigit >= '0' and chHexDigit <= '9'):
        nHexDigit = ord(chHexDigit) - ord('0')
    elif (chHexDigit >= 'A' and chHexDigit <= 'F'):
        nHexDigit = 10 + ord(chHexDigit) - ord('A')
    elif (chHexDigit >= 'a' and chHexDigit <= 'f'):
        nHexDigit = 10 + ord(chHexDigit) - ord('a')
    nDecNum += (nHexDigit * nHexPower)
    nHexPower *= 16
print(f"The decimal equivalent of the hexadecimal number "
      f"{strLine} is {nDecNum}")
