class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort() 
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue                
                path.append(candidate)
                backtrack(i + 1, remaining - candidate, path)
                path.pop()        
        backtrack(0, target, [])
        return result
if __name__ == "__main__":
    solution = Solution()
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(solution.combinationSum2(candidates1, target1))
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(solution.combinationSum2(candidates2, target2))
print(__name__)