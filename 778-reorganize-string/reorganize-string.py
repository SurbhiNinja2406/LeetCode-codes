import heapq
from collections import Counter


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        count = Counter(s)
        max_freq = max(count.values())
        if max_freq > (n + 1) // 2:
            return ""
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)
        result = []
        prev_freq, prev_ch = 0, ''
        while heap:
            freq, ch = heapq.heappop(heap)
            result.append(ch)
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))
            prev_freq, prev_ch = freq + 1, ch
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print("Input: s = {}".format(s))
    print("Output: {}".format(sol.reorganizeString(s)))
    print("Expected: aba (or any valid rearrangement)\n")
    s = "aaab"
    print("Input: s = {}".format(s))
    print("Output: '{}'".format(sol.reorganizeString(s)))
    print("Expected: '' (empty string)\n")