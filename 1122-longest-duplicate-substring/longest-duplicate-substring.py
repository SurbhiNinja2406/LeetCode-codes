class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        BASE = 26
        MOD = (1 << 61) - 1       
        def search(L):
            h = 0
            for i in range(L):
                h = (h * BASE + nums[i]) % MOD
            seen = {h: [0]}         
            pow_L = pow(BASE, L, MOD)
            for start in range(1, n - L + 1):
                h = (h * BASE - nums[start - 1] * pow_L + nums[start + L - 1]) % MOD
                if h in seen:
                    sub = s[start:start + L]
                    for prev in seen[h]:
                        if s[prev:prev + L] == sub:  
                            return start
                    seen[h].append(start)
                else:
                    seen[h] = [start]
            return -1
        lo, hi = 1, n - 1
        best_start, best_len = 0, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                best_start, best_len = idx, mid   
                lo = mid + 1                    
            else:
                hi = mid - 1           
        return s[best_start:best_start + best_len] if best_len else ""
if __name__ == "__main__":
    sol = Solution()
    def is_valid(s, result, expected_len):
        if len(result) != expected_len:
            return False
        if expected_len == 0:
            return True
        first = s.find(result)
        return first != -1 and s.find(result, first + 1) != -1  
    tests = [
        ("banana", 3),
        ("abcd", 0),
        ("aaaaa", 4),      
    ]
    for s, expected_len in tests:
        result = sol.longestDupSubstring(s)
        status = "PASS" if is_valid(s, result, expected_len) else "FAIL"
        print("{}: got '{}'".format(status, result))
print(__name__)