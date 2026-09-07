class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        n = len(s)
        result = list(s)
        total_shift = 0
        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            original_pos = ord(result[i]) - ord('a')
            new_pos = (original_pos + total_shift) % 26
            result[i] = chr(new_pos + ord('a'))
        return ''.join(result)
if __name__ == "__main__":
    solution = Solution()
    s1, shifts1 = "abc", [3, 5, 9]
    print(solution.shiftingLetters(s1, shifts1))  
    s2, shifts2 = "aaa", [1, 2, 3]
    print(solution.shiftingLetters(s2, shifts2)) 
    s3, shifts3 = "z", [1]
    print(solution.shiftingLetters(s3, shifts3))  
    s4, shifts4 = "ab", [1000000000, 1000000000]
    print(solution.shiftingLetters(s4, shifts4))
    s5, shifts5 = "hello", [0, 0, 0, 0, 0]
    print(solution.shiftingLetters(s5, shifts5))  
print(__name__)