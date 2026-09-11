from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.requests = deque()
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
if __name__ == "__main__":
    recentCounter = RecentCounter()
    calls = [1, 100, 3001, 3002]
    expected = [1, 2, 3, 3]
    all_ok = True
    for t, exp in zip(calls, expected):
        result = recentCounter.ping(t)
        status = "OK" if result == exp else "FAIL"
        all_ok = all_ok and (result == exp)
        print("ping({}) -> {}  (expected {})  {}".format(t, result, exp, status))
    print("\nAll test cases passed!" if all_ok else "\nSome test cases FAILED.")
    import time
    rc2 = RecentCounter()
    t_start = time.time()
    for i in range(1, 10001):
        rc2.ping(i * 100) 
    elapsed = time.time() - t_start
    print("\nStress test: 10000 calls completed in {:.4f} seconds".format(elapsed))
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)