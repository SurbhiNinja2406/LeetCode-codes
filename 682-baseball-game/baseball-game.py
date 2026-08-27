class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.calPoints(["5", "2", "C", "D", "+"])
    print("Example 1:")
    print('Input:  ops = ["5","2","C","D","+"]')
    print("Output:", result1)
    print("Expected: 30")
    print()
    result2 = solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print("Example 2:")
    print('Input:  ops = ["5","-2","4","C","D","9","+","+"]')
    print("Output:", result2)
    print("Expected: 27")
    print()
    result3 = solution.calPoints(["1", "C"])
    print("Example 3:")
    print('Input:  ops = ["1","C"]')
    print("Output:", result3)
    print("Expected: 0")
    print()
    result4 = solution.calPoints(["10"])
    print("Example 4 (extra):")
    print('Input:  ops = ["10"]')
    print("Output:", result4)
    print("Expected: 10")
    print()
    result5 = solution.calPoints(["1", "D", "D", "D"])
    print("Example 5 (extra):")
    print('Input:  ops = ["1","D","D","D"]')
    print("Output:", result5)
    print("Expected: 15")  
    print()
    result6 = solution.calPoints(["-1", "-2", "+"])
    print("Example 6 (extra):")
    print('Input:  ops = ["-1","-2","+"]')
    print("Output:", result6)
    print("Expected: -6") 
print(__name__)