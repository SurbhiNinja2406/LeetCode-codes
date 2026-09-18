class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        level = 0
        while (1 << (level + 1)) <= label:
            level += 1
        path = []
        current = label
        while level >= 0:
            path.append(current)
            if level == 0:
                break
            start = 1 << level
            end = (1 << (level + 1)) - 1
            mirrored = start + end - current
            current = mirrored // 2
            level -= 1
        path.reverse()
        return path
if __name__ == "__main__":
    sol = Solution()
    print(sol.pathInZigZagTree(14))  
    print(sol.pathInZigZagTree(26))
print(__name__)