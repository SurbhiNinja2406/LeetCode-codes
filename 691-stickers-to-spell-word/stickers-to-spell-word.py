from collections import Counter
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = len(target)
        full_mask = (1 << n) - 1
        sticker_counters = [Counter(s) for s in stickers]
        target_letters = set(target)
        sticker_counters = [
            c for c in sticker_counters if target_letters & set(c.keys())
        ]
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == float('inf'):
                continue
            for counter in sticker_counters:
                sticker_copy = counter.copy()
                new_mask = mask
                for i in range(n):
                    if new_mask & (1 << i):
                        continue 
                    ch = target[i]
                    if sticker_copy.get(ch, 0) > 0:
                        sticker_copy[ch] -= 1
                        new_mask |= (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        return dp[full_mask] if dp[full_mask] != float('inf') else -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.minStickers(["with", "example", "science"], "thehat"))  
    print(sol.minStickers(["notice", "possible"], "basicbasic"))     
print(__name__)