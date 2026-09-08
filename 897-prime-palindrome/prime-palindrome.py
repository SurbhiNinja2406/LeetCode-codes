class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def is_prime(num):
            if num < 2:
                return False
            if num < 4:
                return True
            if num % 2 == 0:
                return False
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True
        
        # Key insight: Any palindrome with an EVEN number of digits
        # (other than single digits) is always divisible by 11.
        # Proof: For an even-length palindrome, digits mirror around the center,
        # so alternating sum (used in divisibility rule for 11) always cancels to 0.
        # Therefore, we can SKIP all even-length palindromes (except handle 11 itself)
        # since they can never be prime (except 11, which we handle via direct check
        # since n could start below 11).
        
        if n <= 2:
            return 2
        
        # Handle case where n is very small - check up to 11 directly since
        # skipping even-length ranges could jump past small answers.
        if n <= 11:
            for candidate in range(n, 12):
                if is_prime(candidate) and str(candidate) == str(candidate)[::-1]:
                    return candidate
        length = len(str(n))
        if length % 2 == 0:
            length += 1        
        while True:
            half_length = (length + 1) // 2
            start = 10 ** (half_length - 1)
            end = 10 ** half_length            
            for half in range(start, end):
                half_str = str(half)
                palindrome_str = half_str + half_str[-2::-1]
                candidate = int(palindrome_str)
                if candidate < n:
                    continue                
                if is_prime(candidate):
                    return candidate
            length += 2
if __name__ == "__main__":
    sol = Solution()
    n1 = 6
    result1 = sol.primePalindrome(n1)
    print("Example 1:")
    print("Input: n = {}".format(n1))
    print("Output:", result1)
    print("Expected: 7")
    print()
    n2 = 8
    result2 = sol.primePalindrome(n2)
    print("Example 2:")
    print("Input: n = {}".format(n2))
    print("Output:", result2)
    print("Expected: 11")
    print()
    n3 = 13
    result3 = sol.primePalindrome(n3)
    print("Example 3:")
    print("Input: n = {}".format(n3))
    print("Output:", result3)
    print("Expected: 101")
    print()
    n4 = 9989900
    result4 = sol.primePalindrome(n4)
    print("Additional test:")
    print("Input: n = {}".format(n4))
    print("Output:", result4)
print(__name__)