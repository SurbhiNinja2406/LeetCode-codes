from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_set = set(deadends)
        start = "0000"
        if start in dead_set:
            return -1
        if target == start:
            return 0
        def neighbors(state):
            for i in range(4):
                digit = int(state[i])
                for delta in (1, -1):
                    new_digit = (digit + delta) % 10
                    yield state[:i] + str(new_digit) + state[i+1:]
        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            state, turns = queue.popleft()
            for nxt in neighbors(state):
                if nxt in visited or nxt in dead_set:
                    continue
                if nxt == target:
                    return turns + 1
                visited.add(nxt)
                queue.append((nxt, turns + 1))
        return -1
if __name__ == "__main__":
    solution = Solution()
    deadends1 = ["0201", "0101", "0102", "1212", "2002"]
    target1 = "0202"
    result1 = solution.openLock(deadends1, target1)
    print("Example 1: Output = {0}, Expected = 6".format(result1))
    assert result1 == 6
    deadends2 = ["8888"]
    target2 = "0009"
    result2 = solution.openLock(deadends2, target2)
    print("Example 2: Output = {0}, Expected = 1".format(result2))
    assert result2 == 1
    deadends3 = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target3 = "8888"
    result3 = solution.openLock(deadends3, target3)
    print("Example 3: Output = {0}, Expected = -1".format(result3))
    assert result3 == -1
    print("\nAll test cases passed!")
print(__name__)