class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        current = list(range(1, 10))        
        for _ in range(n - 1):
            next_level = []
            for num in current:
                last_digit = num % 10
                next_digit_up = last_digit + k
                if next_digit_up <= 9:
                    next_level.append(num * 10 + next_digit_up)
                next_digit_down = last_digit - k
                if k != 0 and next_digit_down >= 0:
                    next_level.append(num * 10 + next_digit_down)            
            current = next_level        
        return current
if __name__ == "__main__":
    sol = Solution()
    n1, k1 = 3, 7
    result1 = sol.numsSameConsecDiff(n1, k1)
    expected1 = [181, 292, 707, 818, 929]
    print("Input: n={}, k={}".format(n1, k1))
    print("Output: {}".format(sorted(result1)))
    print("Expected: {}".format(sorted(expected1)))
    print("Pass: {}\n".format(sorted(result1) == sorted(expected1)))
    n2, k2 = 2, 1
    result2 = sol.numsSameConsecDiff(n2, k2)
    expected2 = [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    print("Input: n={}, k={}".format(n2, k2))
    print("Output: {}".format(sorted(result2)))
    print("Expected: {}".format(sorted(expected2)))
    print("Pass: {}\n".format(sorted(result2) == sorted(expected2)))
    n3, k3 = 2, 0
    result3 = sol.numsSameConsecDiff(n3, k3)
    expected3 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    print("Input: n={}, k={}".format(n3, k3))
    print("Output: {}".format(sorted(result3)))
    print("Expected: {}".format(sorted(expected3)))
    print("Pass: {}\n".format(sorted(result3) == sorted(expected3)))
    n4, k4 = 2, 9
    result4 = sol.numsSameConsecDiff(n4, k4)
    expected4 = [19, 90]
    print("Input: n={}, k={}".format(n4, k4))
    print("Output: {}".format(sorted(result4)))
    print("Expected: {}".format(sorted(expected4)))
    print("Pass: {}\n".format(sorted(result4) == sorted(expected4)))
    n5, k5 = 2, 8
    result5 = sol.numsSameConsecDiff(n5, k5)
    expected5 = [0 if False else 19, 90, 17, 19, 28, 90] 
    result5 = sol.numsSameConsecDiff(n5, k5)
    print("Input: n={}, k={}".format(n5, k5))
    print("Output: {}".format(sorted(result5)))