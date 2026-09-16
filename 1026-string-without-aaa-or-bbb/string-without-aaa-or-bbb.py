class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        result = []
        while a > 0 or b > 0:
            last_two_same_a = len(result) >= 2 and result[-1] == result[-2] == 'a'
            last_two_same_b = len(result) >= 2 and result[-1] == result[-2] == 'b'
            if last_two_same_a:
                result.append('b')
                b -= 1
            elif last_two_same_b:
                result.append('a')
                a -= 1
            else:
                if a >= b:
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1
        return ''.join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.strWithout3a3b(1, 2))  
    print(sol.strWithout3a3b(4, 1))  
print(__name__)