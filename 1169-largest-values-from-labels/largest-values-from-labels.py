class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        items = sorted(zip(values, labels), key=lambda x: -x[0])
        label_count = {}
        total = 0
        chosen = 0
        for value, label in items:
            if chosen >= numWanted:
                break
            count = label_count.get(label, 0)
            if count < useLimit:
                total += value
                label_count[label] = count + 1
                chosen += 1
        return total
if __name__ == "__main__":
    solution = Solution()
    values1 = [5, 4, 3, 2, 1]
    labels1 = [1, 1, 2, 2, 3]
    numWanted1 = 3
    useLimit1 = 1
    result1 = solution.largestValsFromLabels(values1, labels1, numWanted1, useLimit1)
    print("Example 1: {} (Expected: 9)".format(result1))
    values2 = [5, 4, 3, 2, 1]
    labels2 = [1, 3, 3, 3, 2]
    numWanted2 = 3
    useLimit2 = 2
    result2 = solution.largestValsFromLabels(values2, labels2, numWanted2, useLimit2)
    print("Example 2: {} (Expected: 12)".format(result2))
    values3 = [9, 8, 8, 7, 6]
    labels3 = [0, 0, 0, 1, 1]
    numWanted3 = 3
    useLimit3 = 1
    result3 = solution.largestValsFromLabels(values3, labels3, numWanted3, useLimit3)
    print("Example 3: {} (Expected: 16)".format(result3))
print(__name__)