class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        def next_day(state):
            new_state = [0] * len(state)
            for i in range(1, len(state) - 1):
                if state[i - 1] == state[i + 1]:
                    new_state[i] = 1
                else:
                    new_state[i] = 0
            return new_state        
        if n == 0:
            return cells        
        seen = {}  
        state = list(cells)
        day = 0        
        while day < n:
            state_tuple = tuple(state)
            if state_tuple in seen:
                cycle_start = seen[state_tuple]
                cycle_length = day - cycle_start
                remaining = (n - cycle_start) % cycle_length
                state = list(cells)
                target_day = cycle_start + remaining
                state = list(cells)
                for _ in range(target_day):
                    state = next_day(state)
                return state            
            seen[state_tuple] = day
            state = next_day(state)
            day += 1        
        return state
if __name__ == "__main__":
    sol = Solution()
    cells1 = [0, 1, 0, 1, 1, 0, 0, 1]
    n1 = 7
    result1 = sol.prisonAfterNDays(cells1, n1)
    expected1 = [0, 0, 1, 1, 0, 0, 0, 0]
    print("Input: cells={}, n={}".format(cells1, n1))
    print("Output: {}".format(result1))
    print("Expected: {}".format(expected1))
    print("Pass: {}\n".format(result1 == expected1))
    cells2 = [1, 0, 0, 1, 0, 0, 1, 0]
    n2 = 1000000000
    result2 = sol.prisonAfterNDays(cells2, n2)
    expected2 = [0, 0, 1, 1, 1, 1, 1, 0]
    print("Input: cells={}, n={}".format(cells2, n2))
    print("Output: {}".format(result2))
    print("Expected: {}".format(expected2))
    print("Pass: {}\n".format(result2 == expected2))
    cells3 = [0, 1, 0, 1, 1, 0, 0, 1]
    n3 = 1
    result3 = sol.prisonAfterNDays(cells3, n3)
    expected3 = [0, 1, 1, 0, 0, 0, 0, 0]
    print("Input: cells={}, n={}".format(cells3, n3))
    print("Output: {}".format(result3))
    print("Expected: {}".format(expected3))
    print("Pass: {}\n".format(result3 == expected3))
    cells4 = [1, 1, 1, 1, 1, 1, 1, 1]
    n4 = 3
    result4 = sol.prisonAfterNDays(cells4, n4)
    print("Input: cells={}, n={}".format(cells4, n4))
    print("Output: {}".format(result4))
    cells5 = [0, 0, 0, 0, 0, 0, 0, 0]
    n5 = 1000000000
    result5 = sol.prisonAfterNDays(cells5, n5)
    print("Input: cells={}, n={}".format(cells5, n5))
    print("Output: {}".format(result5))
print(__name__)