class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}        
        for rod in rods:
            new_dp = dict(dp)  
            for diff, taller in dp.items():
                shorter = taller - diff
                new_diff_a = diff + rod
                new_taller_a = taller + rod
                if new_diff_a not in new_dp or new_dp[new_diff_a] < new_taller_a:
                    new_dp[new_diff_a] = new_taller_a
                new_shorter_b = shorter + rod
                new_taller_b = max(taller, new_shorter_b)
                new_diff_b = abs(taller - new_shorter_b)
                if new_diff_b not in new_dp or new_dp[new_diff_b] < new_taller_b:
                    new_dp[new_diff_b] = new_taller_b
            
            dp = new_dp
        
        return dp.get(0, 0)


if __name__ == "__main__":
    sol = Solution()
    rods1 = [1, 2, 3, 6]
    result1 = sol.tallestBillboard(rods1)
    print("Input: {}".format(rods1))
    print("Output: {}".format(result1))
    print("Expected: 6")
    print("Pass: {}\n".format(result1 == 6))
    rods2 = [1, 2, 3, 4, 5, 6]
    result2 = sol.tallestBillboard(rods2)
    print("Input: {}".format(rods2))
    print("Output: {}".format(result2))
    print("Expected: 10")
    print("Pass: {}\n".format(result2 == 10))
    rods3 = [1, 2]
    result3 = sol.tallestBillboard(rods3)
    print("Input: {}".format(rods3))
    print("Output: {}".format(result3))
    print("Expected: 0")
    print("Pass: {}\n".format(result3 == 0))
    rods4 = [5]
    result4 = sol.tallestBillboard(rods4)
    print("Input: {}".format(rods4))
    print("Output: {}".format(result4))
    print("Expected: 0")
    print("Pass: {}\n".format(result4 == 0))
    rods5 = [7, 7]
    result5 = sol.tallestBillboard(rods5)
    print("Input: {}".format(rods5))
    print("Output: {}".format(result5))
    print("Expected: 7")
    print("Pass: {}\n".format(result5 == 7))
    rods6 = [2, 2, 3, 3]
    result6 = sol.tallestBillboard(rods6)
    print("Input: {}".format(rods6))
    print("Output: {}".format(result6))
    print("Expected: 5")
    print("Pass: {}\n".format(result6 == 5))
print(__name__)