class Solution:


    def myAtoi(self, s: str) -> int:

        # Ignore any leading whitespace (" ").
        s = s.lstrip()

        if s == "":
            return 0

        # check sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # conversion: skip leading 0
        s = s.lstrip('0')

        if s == "":
            return 0

        if not s[0].isdigit():
            return 0

        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break

        if (sign == 1 and int(s) >= 2147483647):
            return 2147483647
        elif (sign == -1 and -1 * int(s) <= -2147483648):
            return -2147483648
        else: 
            return int(s) if sign == 1 else -1 * int(s)