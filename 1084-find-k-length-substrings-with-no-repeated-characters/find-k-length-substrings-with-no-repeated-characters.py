class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k > n:
            return 0
        count = {}
        distinct = 0
        result = 0
        for i in range(n):
            c = s[i]
            count[c] = count.get(c, 0) + 1
            if count[c] == 1:
                distinct += 1
            if i >= k:
                left_c = s[i - k]
                count[left_c] -= 1
                if count[left_c] == 0:
                    distinct -= 1
            if i >= k - 1:
                if distinct == k:
                    result += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    s1, k1 = "havefunonleetcode", 5
    print(sol.numKLenSubstrNoRepeats(s1, k1))  
    s2, k2 = "home", 5
    print(sol.numKLenSubstrNoRepeats(s2, k2))  
print(__name__)