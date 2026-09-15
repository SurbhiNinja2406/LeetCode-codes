class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1  
            score[b] += 1  
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.findJudge(2, [[1, 2]]))  
    print(sol.findJudge(3, [[1, 3], [2, 3]])) 
    print(sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(__name__)