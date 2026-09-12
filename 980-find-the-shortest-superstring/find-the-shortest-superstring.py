class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                max_len = min(len(a), len(b))
                for k in range(max_len, 0, -1):
                    if a[-k:] == b[:k]:
                        overlap[i][j] = k
                        break
        dp = [[0] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                prev_mask = mask ^ (1 << i)
                if prev_mask == 0:
                    continue
                for j in range(n):
                    if not (prev_mask & (1 << j)):
                        continue
                    candidate = dp[prev_mask][j] + overlap[j][i]
                    if candidate >= dp[mask][i]:
                        dp[mask][i] = candidate
                        parent[mask][i] = j
        full_mask = (1 << n) - 1
        best_last = max(range(n), key=lambda i: dp[full_mask][i])
        order = []
        mask = full_mask
        last = best_last
        while last != -1:
            order.append(last)
            prev_last = parent[mask][last]
            mask ^= (1 << last)
            last = prev_last
        order.reverse()
        result = words[order[0]]
        for idx in range(1, len(order)):
            prev_word_idx = order[idx - 1]
            curr_word_idx = order[idx]
            ov = overlap[prev_word_idx][curr_word_idx]
            result += words[curr_word_idx][ov:]
        return result
if __name__ == "__main__":
    sol = Solution()
    words1 = ["alex", "loves", "leetcode"]
    print(sol.shortestSuperstring(words1))  
    words2 = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    print(sol.shortestSuperstring(words2)) 
print(__name__)