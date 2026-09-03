class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        same = {'0', '1', '8'}
        different = {'2', '5', '6', '9'}
        invalid = {'3', '4', '7'}
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            has_invalid = False
            has_different = False
            for ch in s:
                if ch in invalid:
                    has_invalid = True
                    break
                elif ch in different:
                    has_different = True
            if not has_invalid and has_different:
                count += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotatedDigits(10)) 
    print(sol.rotatedDigits(1))  
    print(sol.rotatedDigits(2)) 
print(__name__)