class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)
        score = 0
        max_length = 0
        first_occurrence = {}        
        for i in range(n):
            score += 1 if hours[i] > 8 else -1            
            if score > 0:
                max_length = i + 1
            else:
                if (score - 1) in first_occurrence:
                    candidate_length = i - first_occurrence[score - 1]
                    max_length = max(max_length, candidate_length)
            if score not in first_occurrence:
                first_occurrence[score] = i        
        return max_length
if __name__ == "__main__":
    solution = Solution()
    hours1 = [9, 9, 6, 0, 6, 6, 9]
    result1 = solution.longestWPI(hours1)
    print("Example 1: {} (Expected: 3)".format(result1))
    hours2 = [6, 6, 6]
    result2 = solution.longestWPI(hours2)
    print("Example 2: {} (Expected: 0)".format(result2))
print(__name__)