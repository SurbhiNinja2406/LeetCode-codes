class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            return ""
        need = Counter(t)
        required = len(need)  
        left = 0
        formed = 0  
        window_counts = {}
        best_len = float('inf')
        best_left = 0
        best_right = 0        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in need and window_counts[char] == need[char]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                    best_right = right
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in need and window_counts[left_char] < need[left_char]:
                    formed -= 1                
                left += 1        
        return "" if best_len == float('inf') else s[best_left:best_right + 1]
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC")) 
    print(sol.minWindow("a", "a")) 
    print(sol.minWindow("a", "aa"))
print(__name__)