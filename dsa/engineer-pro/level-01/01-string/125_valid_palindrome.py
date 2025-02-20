class Solution:
    # def reverse(self, s: str) -> str:
    #     n = len(s)
    #     reverseStr = ""
    #     for i in range(n - 1, -1, -1): # loop from n-1 to before -1, step -1
    #         reverseStr += s[i]
    #     return reverseStr
    
    def isPalindrome(self, s: str) -> bool:
        alphaNumericStr = ''.join([c if c.isalpha() or c.isdigit() else '' for c in s])
        # for c in s:
        #     if c.isalpha() or c.isdigit():
        #         alphaNumericStr += c

        alphaNumericStr = alphaNumericStr.lower()

        # return alphaNumericStr == self.reverse(alphaNumericStr)
        return alphaNumericStr == alphaNumericStr[::-1] # (start, end, step)