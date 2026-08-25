class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])        
        merged = [intervals[0]]        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)        
        return merged
if __name__ == "__main__":
    solution = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals1))  
    intervals2 = [[1,4],[4,5]]
    print(solution.merge(intervals2)) 
    intervals3 = [[4,7],[1,4]]
    print(solution.merge(intervals3)) 
print(__name__)