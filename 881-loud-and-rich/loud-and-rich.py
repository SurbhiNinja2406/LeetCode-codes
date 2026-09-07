from collections import defaultdict


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)  
        answer = [-1] * n
        memo = {}
        def dfs(person):
            if person in memo:
                return memo[person]
            quietest = person 
            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate
            memo[person] = quietest
            return quietest
        for person in range(n):
            answer[person] = dfs(person)
        return answer
if __name__ == "__main__":
    solution = Solution()
    richer1 = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet1 = [3, 2, 5, 4, 6, 1, 7, 0]
    print(solution.loudAndRich(richer1, quiet1)) 
    richer2 = []
    quiet2 = [0]
    print(solution.loudAndRich(richer2, quiet2))  
    richer3 = [[0, 1], [1, 2], [2, 3]]
    quiet3 = [3, 2, 1, 0]
    print(solution.loudAndRich(richer3, quiet3))
    richer4 = []
    quiet4 = [5, 3, 1, 4, 2]
    print(solution.loudAndRich(richer4, quiet4))  
print(__name__)