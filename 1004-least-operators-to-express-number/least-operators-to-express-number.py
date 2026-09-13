class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        memo = {}        
        def dp(target):
            if x > target:
                return min(target * 2 - 1, (x - target) * 2)            
            if target in memo:
                return memo[target]
            k = 1
            p = x
            while p < target:         
                p *= x
                k += 1            
            if p == target:
                ans = k - 1
            elif p - target < target:
                ans = min((k - 1) + dp(target - p // x), k + dp(p - target))
            else:
                ans = (k - 1) + dp(target - p // x)            
            memo[target] = ans
            return ans        
        return dp(target)
if __name__ == "__main__":
    sol = Solution()
    x1, target1 = 3, 19
    result1 = sol.leastOpsExpressTarget(x1, target1)
    print("Input: x={}, target={}".format(x1, target1))
    print("Output: {}".format(result1))
    print("Expected: 5")
    print("Pass: {}\n".format(result1 == 5))
    x2, target2 = 5, 501
    result2 = sol.leastOpsExpressTarget(x2, target2)
    print("Input: x={}, target={}".format(x2, target2))
    print("Output: {}".format(result2))
    print("Expected: 8")
    print("Pass: {}\n".format(result2 == 8))
    x3, target3 = 100, 100000000
    result3 = sol.leastOpsExpressTarget(x3, target3)
    print("Input: x={}, target={}".format(x3, target3))
    print("Output: {}".format(result3))
    print("Expected: 3")
    print("Pass: {}\n".format(result3 == 3))
print(__name__)