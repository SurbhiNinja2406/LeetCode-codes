class Solution(object):
    def combinationSum(self, candidates, target):
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
                path.append(candidate)
                backtrack(i, remaining - candidate, path)
                path.pop()        
        backtrack(0, target, [])
        return result
if __name__ == "__main__":
    solution = Solution()
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(solution.combinationSum(candidates1, target1))  
    candidates2 = [2, 3, 5]
    target2 = 8
    print(solution.combinationSum(candidates2, target2))  
    candidates3 = [2]
    target3 = 1
    print(solution.combinationSum(candidates3, target3))  
print(__name__)