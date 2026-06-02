class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for ch in s:

            if ch.isalnum():
                newString += ch.lower()
        palindrome = ""
        for i in range(len(newString)-1,-1,-1):
            palindrome= palindrome + newString[i]
        if (palindrome==newString):
            return True
        return False 
            