class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        n = len(stones)
        max_moves = max(stones[-1] - stones[1], stones[-2] - stones[0]) - (n - 2)
        min_moves = n
        i = 0
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            count = j - i + 1  
            if count == n - 1 and stones[j] - stones[i] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - count)
        return [min_moves, max_moves]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([7, 4, 9], [1, 2]),
        ([6, 5, 4, 3, 10], [2, 3]),
        ([2, 3, 4], [0, 0]),         
    ]
    for stones, expected in tests:
        result = sol.numMovesStonesII(stones)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)