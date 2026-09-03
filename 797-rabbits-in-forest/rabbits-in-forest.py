class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = {}
        for a in answers:
            count[a] = count.get(a, 0) + 1
        total = 0
        for answer, freq in count.items():
            group_size = answer + 1
            groups_needed = (freq + group_size - 1) // group_size
            total += groups_needed * group_size
        return total
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 1, 2], 5),
        ([10, 10, 10], 11),
        ([0], 1),
        ([0, 0, 1, 1, 1], 6),
        ([], 0),
    ]
    for i, (answers, expected) in enumerate(test_cases, 1):
        result = sol.numRabbits(answers)
        status = "PASS" if result == expected else "FAIL"
        print("Test " + str(i) + ": answers=" + str(answers) +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)