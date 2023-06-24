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

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# my conclusion
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestLength = len(strs[0])
        smallestWord = ""
        if len(strs) == 1 :
            return strs[0]
        if "" in strs :
            index = strs.index("")
            return strs[index]
        for word in strs :
            if(smallestLength >= len(word)) :
                smallestLength = len(word)
                smallestWord = word

        matchedString = ""
        for index in range(1, (smallestLength + 1)) :
            for word in strs :
                if not (word[:index] == smallestWord[:index]) :
                    return matchedString
            matchedString = smallestWord[:index]
        return matchedString


# TheLegend27
class Solution: # 16ms 
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        s1, s2, res = strs[0], strs[-1], ""

        for i in range (len(s1)):
            if s1[i] == s2[i]:
                res += s1[i]
            else:
                break
        return res

class Solution: # one liner
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(a[0] for a in takewhile(lambda x: len(set(x)) == 1, zip(*strs)))
    
##############################################################################################################

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if: Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

# my conclusion
class Solution: # 52ms and 16.4mb 
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2 or len(s) % 2 == 1:
            return False
        for index in s :
            if index == '(' or index == '[' or index == '{':
                stack.append(index)
            elif stack == [] and (index == ')' or index == ']' or index == '}') :
                return False
            elif stack[len(stack) - 1] == '(' and index == ')' and '(' in stack :
                stack.pop()
            elif stack[len(stack) - 1] == '[' and index == ']' and '[' in stack :
                stack.pop()
            elif stack[len(stack) - 1] == '{' and index == '}' and '{' in stack :
                stack.pop()
            else :
                return False
        if stack == [] :
            return True
        else :
            return False
        
#TheLegend27
class Solution: # 14ms 
    def isValid(self, s: str) -> bool:
        pMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
            }
        stack = []

        for c in s:
            if c not in pMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != pMap[c]:
                return False
            stack.pop()

        return not stack
    
class Solution: # 13.4mb 
    def isValid(self, s: str) -> bool:
        hmap = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        stack = []
        for c in s:
            if c in hmap.values():
                stack.append(c)
            elif c in hmap:
                if stack == [] or hmap[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
    
#########################################################################################################

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# my conclusion 
class Solution: # 121ms 16.4mb
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        dict1 = {}
        pattern1 = ""
        for letter in str1: 
            pattern1 = pattern1 + letter 
            str1_copy = str1
            count = 0
            while len(str1_copy) > 0:
                if(str1_copy[(len(str1_copy) - (len(pattern1))):] == pattern1) :
                    count += 1
                    str1_copy = str1_copy[:(len(str1_copy) - len(pattern1))]
                    if(str1_copy == "") :
                        break
                else :
                    break
            if (count * len(pattern1) == len(str1)) :
                dict1[f"{pattern1}"] = count
        dict1Lists = list(dict1.items())

        dict2 = {}
        pattern2 = ""
        for letter in str2: 
            pattern2 = pattern2 + letter 
            str2_copy = str2
            count = 0
            while len(str2_copy) > 0:
                if(str2_copy[(len(str2_copy) - (len(pattern2))):] == pattern2) :
                    count += 1
                    str2_copy = str2_copy[:(len(str2_copy) - len(pattern2))]
                    if(str2_copy == "") :
                        break
                else :
                    break
            if (count * len(pattern2) == len(str2)) :
                dict2[f"{pattern2}"] = count

        for key, value in dict2.items() :
            for i in dict1Lists :
                if key == i[0] :  
                    pattern1 = pattern2 = key

        if(pattern1 == pattern2) :
            return pattern1
        else :
            return ""

# TheLegend27
class Solution: # 22ms 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while True:
            if str1 == str2:
                return str1
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if not str1.startswith(str2):
                break
            str1, str2 = str2, str1[len(str2):]
        return ""

class Solution: # 13.7mb
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)),0 , -1):
            l = len(str1[:i])
            if len(str1) % l != 0 or len(str2) % l != 0:
                continue
            l1 = len(str1) // l
            l2 = len(str2) // l
            
            if str1[:i] * l1 == str1 and str1[:i] * l2  == str2:
                return str1[:i] 

        return ''

######################################################################################################

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# my conclusion 
class Solution: # 97ms 16.7mb
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1 + nums2
        mergedArray.sort()
        middle = int(len(mergedArray)/2) + 1
        if (len(mergedArray) % 2 == 1) :
            return mergedArray[(len(mergedArray) - middle)]
        else : 
            return (mergedArray[len(mergedArray) - middle + 1] + mergedArray[len(mergedArray) - middle]) / 2
        
# TheLegend27
class Solution: # 71ms
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()

        if len(nums3) % 2 == 0:
            return (nums3[len(nums3)//2] + nums3[(len(nums3)//2) - 1]) / 2
        return nums3[len(nums3)//2]

class Solution: # 14mb
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = median(sorted(nums1 + nums2))
        return result
    
###########################################################################################################

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# my conclusion : AI helped me , couldn't figure out how to reduce this one.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        biggestWater = 0

        while left < right:
            w = right - left
            smallerH = min(height[left], height[right])
            currWater = w * smallerH

            biggestWater = max(biggestWater, currWater)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return biggestWater

# TheLegend27
f = open('user.out', 'w') # 97ms
for h in map(loads, stdin):
    left = 0
    right = len(h) - 1
    d = right - left
    max_s = 0
    max_h = max(h)
    while left < right and (max_h * d > max_s):
        d = right - left
        max_s = max(max_s, min(h[left], h[right]) * d)
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1
    print(max_s, file=f)
exit(0)

f = open('user.out', 'w') # 20.8mb
for height in stdin:
    height = loads(height)
    i, j, curr = 0, len(height)-1, -1
    while i <= j:
        cand = (height[i] if height[i] <= height[j] else height[j]) * (j-i)
        if cand > curr:
            curr = cand
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    print(curr, file=f)
exit(0)

#########################################################################################################

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

# my conclusion
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        big = max(candies)
        for kid in candies :
            if kid + extraCandies >= big :
                result.append(True)
            else :
                result.append(False)
        return result

# TheLegend27
class Solution: #19ms
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [True if i+extraCandies >= maxCandies else False for i in candies]
    
class Solution: # 13.6mb
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
    
######################################################################################################

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# my conclusion
class Solution: # 169ms 16.8mb
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = n
        bed = flowerbed
        for i in range(len(bed)) :
            if(flowerbed[i] == 0) :
                if(i > 0):
                    if(bed[i-1] == 1):
                        continue
                if(i < len(bed) - 1):
                    if(bed[i+1] == 1):
                        continue 
                bed[i] = 1
                flowers -= 1
        return True if flowers <= 0 else False
    
# TheLegend27
class Solution: # 141ms
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=1
        f=0
        for i in flowerbed:
            if i:
                c=0
            else:
                c+=1
                if c==3:
                    f+=1
                    c=1
        if not flowerbed[-1]:
            c+=1
            if c==3:
                f+=1
        return f>=n

class Solution: # 14.1mb
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        cnt = 0
        i = 1 
        while i < len(flowerbed)-1:
            prev = flowerbed[i-1]
            nex = flowerbed[i+1]
            curr = flowerbed[i]

            if curr == 0 and prev == 0 and nex == 0:
                cnt += 1
                flowerbed[i] += 1
                i+=1
            i += 1
        return cnt >= n
    
########################################################################################################

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# my conclusion 
class Solution: #  243ms 17.6mb
    def reverseVowels(self, s: str) -> str:
        copy = s 
        vowels = "aeiouAEIOU"
        holder = []
        for i in range(len(copy)) :
            if copy[i] in vowels :
                holder.append(copy[i])
        for i in range(len(copy)) :
            if copy[i] in vowels :
                copy = copy[:i] + holder[len(holder) - 1] + copy[i+1:]
                holder.pop()
        return copy

# TheLegend27
class Solution: # 37ms
    def reverseVowels(self, s: str) -> str:
        dic = "aeiouAEIOU"
        s_list = list(s)
        i = 0
        j = len(s_list) - 1

        while i < j:
            if s_list[i] not in dic:
                i += 1
            elif s_list[j] not in dic:
                j -= 1
            elif s_list[i] in dic and s_list[j] in dic:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1 
                j -= 1

        return "".join(s_list)
    
class Solution: # 14.3mb
    def reverseVowels(self, s: str) -> str:
        vowel_str=""
        output=""
        for i in s:
            if i in "aeiouAEIOU":
                vowel_str+=i
        rev_vowel=vowel_str[::-1]
        x=0
        for i in s:
            if i in "aeiouAEIOU":
                output+=rev_vowel[x]
                x+=1
            else:
                output+=i
        return output
    
#####################################################################################################

