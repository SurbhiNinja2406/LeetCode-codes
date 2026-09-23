class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def pos(c):
            idx = ord(c) - ord('a')
            return idx // 5, idx % 5
        result = []
        cur_row, cur_col = 0, 0 
        for ch in target:
            next_row, next_col = pos(ch)
            dr = next_row - cur_row
            dc = next_col - cur_col
            vertical = ('D' if dr > 0 else 'U') * abs(dr)
            horizontal = ('R' if dc > 0 else 'L') * abs(dc)
            if ch == 'z':
                result.append(horizontal)
                result.append(vertical)
            else:
                result.append(vertical)
                result.append(horizontal)
            result.append('!') 
            cur_row, cur_col = next_row, next_col
        return ''.join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.alphabetBoardPath("leet")) 
    print(sol.alphabetBoardPath("code"))  
print(__name__)