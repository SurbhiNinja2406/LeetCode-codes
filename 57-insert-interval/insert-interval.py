class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1        
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1        
        return result
if __name__ == "__main__":
    solution = Solution()
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    print(solution.insert(intervals1, newInterval1)) 
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print(solution.insert(intervals2, newInterval2))  
print(__name__)