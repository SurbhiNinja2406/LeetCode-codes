class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        left, right = int(left), int(right)
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        count = 0
        MAGIC = 100000 
        for half in range(1, MAGIC):
            s = str(half)
            odd_root = s + s[-2::-1]
            even_root = s + s[::-1]
            for root_str in (odd_root, even_root):
                root = int(root_str)
                square = root * root
                if square > right:
                    continue
                if square < left:
                    continue
                if is_palindrome(square):
                    count += 1
        return count
if __name__ == "__main__":
    solution = Solution()
    left1, right1 = "4", "1000"
    print("Example 1:")
    print("Input: left =", repr(left1), ", right =", repr(right1))
    print("Output:", solution.superpalindromesInRange(left1, right1))
    print()
    left2, right2 = "1", "2"
    print("Example 2:")
    print("Input: left =", repr(left2), ", right =", repr(right2))
    print("Output:", solution.superpalindromesInRange(left2, right2))
print(__name__)