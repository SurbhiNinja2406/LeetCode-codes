class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        n = len(s)
        def is_valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return int(segment) <= 255
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == n:
                    result.append('.'.join(parts))
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if is_valid(segment):
                    parts.append(segment)
                    backtrack(start + length, parts)
                    parts.pop()
        backtrack(0, [])
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("0000"))
    print(sol.restoreIpAddresses("101023"))