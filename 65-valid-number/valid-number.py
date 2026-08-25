class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        seen_sign_after_exponent = False
        seen_digit_after_exponent = False        
        n = len(s)        
        for i in range(n):
            char = s[i]            
            if char.isdigit():
                seen_digit = True
                if seen_exponent:
                    seen_digit_after_exponent = True            
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False            
            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in ('e', 'E'):
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True            
            else:
                return False
        return seen_digit and (not seen_exponent or seen_digit_after_exponent)
if __name__ == "__main__":
    solution = Solution()
    s1 = "0"
    print(solution.isNumber(s1)) 
    s2 = "e"
    print(solution.isNumber(s2))  
    s3 = "."
    print(solution.isNumber(s3)) 
    valid_tests = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
                    "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for t in valid_tests:
        print(t, "->", solution.isNumber(t))  
    invalid_tests = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for t in invalid_tests:
        print(t, "->", solution.isNumber(t))  
print(__name__)