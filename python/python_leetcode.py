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

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# my conclusion 
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
# TheLegend27
class Solution: # 19ms
    def reverseWords(self, s: str) -> str:

        temp=s.split()
        temp.reverse()
        ans=' '.join(temp)
        return ans
    
class Solution: # 16.3mb
    def reverseWords(self, s: str) -> str:
        s.strip()
        l=s.split()
        l=l[::-1]
        return(' '.join(l))
    
############################################################################################

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# helped conclusion 
class Solution: # 248ms 25.7mb
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n 
        suffix_product = [1] * n
        result = [0] * n

        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        for i in range(n):
            result[i] = prefix_product[i] * suffix_product[i]
        return result
    
# TheLegend27
sys.stdout = open('user.out', 'w') # 116ms

for nums in map(loads, stdin):
    l, r, n = 1, 1, len(nums) - 1
    output = [1] * len(nums)

    for i, j in zip(range(n), range(n, 0, -1)):
        l *= nums[i]; r *= nums[j]
        output[i + 1] *= l;
        output[j - 1] *= r

    print(f'[{",".join(map(str, output))}]')

exit()

class Solution: # 20.5mb
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_mul = nums.copy()
        for i in range(1, len(nums)):
            prefix_mul[i] = prefix_mul[i - 1] * prefix_mul[i]

        for i in range(len(nums) - 2, -1, -1):
            nums[i] = nums[i + 1] * nums[i]

        for i in range(len(nums)):
            m1 = prefix_mul[i - 1] if i > 0 else 1
            m2 = nums[i + 1] if i < len(nums) - 1 else 1
            nums[i] = m1 * m2 
        return nums
    
######################################################################################
    
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# my helped conclusion 
class Solution: # 1510ms 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets

# TheLegend27
def three_sum(nums): # 222ms
    counts = Counter(nums)
    result = [[0, 0, 0]] if counts[0] >= 3 else []
    nums = [n for n in sorted(counts) if n != 0]
    if not nums or nums[0] > 0 or nums[-1] < 0:
        return result

    if counts[0] >= 1:
        for n in nums:
            if n >= 0:
                break
            if -n in counts:
                result.append([n, 0, -n])
    
    for n in nums:
        if n & 1:
            continue
        remaining = -n >> 1
        if counts[remaining] >= 2:
            result.append([n, remaining, remaining])
    
    for i, n in enumerate(nums):
        kk = -(nums[0] + n)
        if kk < n:
            break
        j = bisect_right(nums, -n << 1) if n < 0 else i + 1
        k = bisect_right(nums, kk)
        for right in nums[j:k]:
            left = -(n + right)
            if left in counts:
                result.append([left, n, right])
    return result

open('user.out', 'w').write("".join(str(three_sum(loads(line))) + "\n" for line in stdin))
exit()

from bisect import bisect_left

class Solution: # 17.3mb
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        prev_n1 = None
        for i, n1 in enumerate(nums[:-2]):
            if n1 == prev_n1:
                continue
            prev_n2 = None
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                n2, n3 = nums[lo], nums[hi]
                if n1 + n2 + n3 < 0:
                    lo += 1
                elif n1 + n2 + n3 > 0:
                    hi -= 1
                else:
                    if n2 != prev_n2:
                        triplets.append((n1, n2, n3))
                        prev_n2 = n2
                    lo += 1
                    hi -= 1
            prev_n1 = n1
        return triplets
    
##########################################################################################

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# my conclusion 
class Solution: # 2404ms & 32.7mb
    def increasingTriplet(self, nums: List[int]) -> bool:
        num = nums
        while len(num) > 2 :
            i = num[0]
            sortNum = sorted(list(set(num)), reverse=True)
            if len(sortNum) < 3 :
                return False
            if i == sortNum[0] or i == sortNum[1] :
                num = num[1:]
                continue
            tempNum = [i] + [x for x in num if x > i] 

            j = 1
            k = len(tempNum) - 1

            while i >= tempNum[j] or tempNum[j] >= tempNum[k] :
                if j == k :
                    break
                for m in range(1, k) :
                    if i < tempNum[j] and tempNum[j] < tempNum[k] :
                        return True
                    j += 1

                k -= 1
                j = 1
            if i < tempNum[j] and tempNum[j] < tempNum[k] :
                return True

            num = num[1:]

        return False
    
# TheLegend27
class Solution: # 982ms
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <=second:
                second = num
            else:
                return True
        return False
    
from bisect import bisect_right, bisect_left
class Solution: # 30mb 
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        # max_heap = []
        stack = []
        for i in range(n):
            """ IDEA: 
            if not stack:
                stack.append(nums[i])
            else:
                idx = bisect_right(stack, nums[i])
                if idx < len(stack):
                    stack[idx] = nums[i]
                else:
                    stack.append(nums[i])
            """
            
            # ReArrange the IDEA into a neat code
            # idx = bisect_right(stack, nums[i])    # BUGGG! at [1,1,1,1,1,1]
            idx = bisect_left(stack, nums[i])       # FIX!!!
            if idx >= len(stack):       # p.s. bisect_left([], 7) outputs 0
                stack.append(nums[i])
            else:
                stack[idx] = nums[i]
        return len(stack) >= 3
    
    
################################################################################################

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# didnt pass , other answer 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ## recursive function 
        def backtrack(first = 1, curr = []) :

            if len(curr) == k : 
                output.append(curr[:])
                return
                
            for i in range(first, n + 1) : 
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        output= []
        backtrack()
        return output
    
###################################################################################################


# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

## bad answer format , conclusion : 
class Solution:
    def compress(self, chars: List[str]) -> int:
        d=[]
        c=1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                c+=1
            else:
                d.append([chars[i-1],c])
                c=1
        d.append([chars[-1],c]) 
        i=0
        for k,v in d:
            chars[i]=k
            i+=1
            if v>1:
                for item in str(v):
                    chars[i]=str(item)
                    i+=1
        return i
    
#################################################################################################

# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)) : 
            backwardsi = len(nums) - 1 - i
            if nums[backwardsi] == 0 :
                for iteration in range(len(nums) - (len(nums)-i)) :
                    if nums[backwardsi+1] : 
                        if nums[backwardsi+1] != 0 : 
                            bucket = nums[backwardsi+1]
                            nums[backwardsi+1] = 0
                            nums[backwardsi] = bucket 
                            backwardsi += 1
         


        """
        Do not return anything, modify nums in-place instead.
        """
# bucket appoach 
# move all zeros to front and keep order
# loop for whole array 
# if zero then move left til can't 
# have bucket to hold 

#####################################################################################################

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" :
            return True
        elif t == "" : 
            return False
        tpointer1 = 0
        tpointer2 = len(t) - 1
        spointer1 = 0
        spointer2 = len(s) - 1
        while tpointer1 <= tpointer2 :
            if s[spointer1] == t[tpointer1] : 
                tpointer1 += 1
                spointer1 += 1
            elif s[spointer2] == t[tpointer2] :
                tpointer2 -= 1
                spointer2 -= 1
            else :
                tpointer1 += 1
                tpointer2 -= 1
        if spointer1 > spointer2 : 
            return True
        else :
            return False


## FIRST TWO POINTERS SOLUTION !!! :)

########################################################################################################

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sortedArr = sorted(nums)
        left = 0
        right = len(sortedArr) - 1
        count = 0
        while left < right : 
            sumNums = sortedArr[left] + sortedArr[right]


            if sumNums == k :
                count += 1
                left += 1
                right -= 1 
            elif sumNums < k :
                left += 1
            else : # sumNums > k : 
                right -= 1

        return count
    
################################################################################################################

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currRunSum = 0
        maxAvg = None

        for i in range(len(nums)) : 

            currRunSum += nums[i]
            if i >= k-1 : # window size = k 
                currAvg = round(float(currRunSum / k), 5)
                if maxAvg == None : 
                    maxAvg = currAvg
                
                maxAvg = max(maxAvg, currAvg)
                currRunSum -= nums[i - (k - 1)] 
        
        return maxAvg
    
##################################################################################################################

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ['a', 'e', 'i', 'o', 'u']
        currNumVs = 0
        currStr = ''
        maxNumVs = 0
        for windowEnd in range(len(s)) : 
            if s[windowEnd] in vowels : 
                currNumVs += 1
            currStr += s[windowEnd]
            if windowEnd >= (k - 1) : 
                maxNumVs = max(maxNumVs, currNumVs)
                if currStr[0] in vowels : 
                    currNumVs -= 1
                currStr = currStr[1:]

        return maxNumVs



# fixed window , str of letters 
# vowel identifier 
# for loop w/ if 

########################################################################################################################