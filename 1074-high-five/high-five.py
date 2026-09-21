from collections import defaultdict
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)
        result = []
        for student_id in sorted(scores):  
            top_five = sorted(scores[student_id], reverse=True)[:5]
            result.append([student_id, sum(top_five) // 5])
        return result
if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]],
        [[1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]],
    ]
    for t in tests:
        print("items = {} -> {}".format(t, sol.highFive(t)))
print(__name__)