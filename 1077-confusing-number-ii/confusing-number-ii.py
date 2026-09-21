class Solution(object):
    def confusingNumberII(self, n):
        """
        :type n: int
        :rtype: int
        """
        rot = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        digits = [0, 1, 6, 8, 9] 
        def dfs(num, rotated, power):
            count = 1 if num != rotated else 0
            for d in digits:
                nxt = num * 10 + d
                if nxt > n:
                    break
                count += dfs(nxt, rot[d] * power + rotated, power * 10)
            return count
        total = 0
        for d in [1, 6, 8, 9]:  
            if d > n:
                break
            total += dfs(d, rot[d], 10)
        return total
if __name__ == "__main__":
    sol = Solution()
    tests = [
        20,  
        100,  
    ]
    for t in tests:
        print("n = {} -> {}".format(t, sol.confusingNumberII(t)))