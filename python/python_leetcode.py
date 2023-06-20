# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# my solution 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        biggerWord = word1 if len(word1) > len(word2) else word2
        smallerWord = word1 if len(word1) < len(word2) else word2
        finalStr = ""
        for index in range(len(smallerWord)) : 
            finalStr = finalStr + word1[index]
            finalStr = finalStr + word2[index]
            if(index == (len(smallerWord) - 1) ) :
                finalStr = finalStr + biggerWord[(index + 1):]
                return finalStr
            
# TheLegend27
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
            
##########################################################################################################

# Given an integer x, return true if x is a palindrome, and false otherwise.

# my solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        regStr = str(x)
        reversedStr = regStr[::-1]
        for index in range(len(regStr)) :
            if regStr[index] == reversedStr[index] :
                continue
            else :
                return False 
        return True
    
# TheLegend27
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
###########################################################################################################

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.

# my solution 
class Solution:
    def romanToInt(self, s: str) -> int:
        totalNum = 0
        count = 0
        while count < len(s) :
            if(s[count] == "M") :
                totalNum += 1000
            elif(s[count:(count + 2)] == "CM") :
                totalNum += 900
                count += 1
            elif(s[count] == "D") :
                totalNum += 500
            elif(s[count:(count + 2)] == "CD") :
                totalNum += 400
                count += 1
            elif(s[count] == "C") :
                totalNum += 100
            elif(s[count:(count + 2)] == "XC") :
                totalNum += 90
                count += 1
            elif(s[count] == "L") :
                totalNum += 50
            elif(s[count:(count + 2)] == "XL") :
                totalNum += 40
                count += 1
            elif(s[count] == "X") :
                totalNum += 10
            elif(s[count:(count + 2)] == "IX") :
                totalNum += 9
                count += 1
            elif(s[count] == "V") :
                totalNum += 5
            elif(s[count:(count + 2)] == "IV") :
                totalNum += 4
                count += 1
            elif(s[count] == "I") :
                totalNum += 1
            else :
                "error"
            count += 1
        return totalNum 

# TheLegend27
class Solution:
    def romanToInt(self, S: str) -> int:
        return sum(S.count(r)*v for r,v in [('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000),('IV',-2),('IX',-2),('XL',-20),('XC',-20),('CD',-200),('CM',-200)])  
		
############################################################################################################

