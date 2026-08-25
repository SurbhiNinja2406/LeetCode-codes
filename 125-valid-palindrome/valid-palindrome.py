class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False            
            left += 1
            right -= 1        
        return True
if __name__ == "__main__":
    sol = Solution()
    s1 = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s1)) 
    s2 = "race a car"
    print(sol.isPalindrome(s2)) 
    s3 = " "
    print(sol.isPalindrome(s3)) 
print(__name__)