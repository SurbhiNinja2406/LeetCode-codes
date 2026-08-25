class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        current_tank = 0
        starting_index = 0        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            if current_tank < 0:
                starting_index = i + 1
                current_tank = 0
        return starting_index if total_tank >= 0 else -1
if __name__ == "__main__":
    sol = Solution()
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(sol.canCompleteCircuit(gas1, cost1))  
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    print(sol.canCompleteCircuit(gas2, cost2))
print(__name__)