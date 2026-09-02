class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
if __name__ == "__main__":
    sol = Solution()
    s = "ababcbacadefegdehijhklij"
    print("Input: s = {}".format(s))
    print("Output: {}".format(sol.partitionLabels(s)))
    print("Expected: [9, 7, 8]\n")
    s = "eccbbbbdec"
    print("Input: s = {}".format(s))
    print("Output: {}".format(sol.partitionLabels(s)))
    print("Expected: [10]\n")
print(__name__)