class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        lo, hi = 0.0, 1.0
        while True:
            mid = (lo + hi) / 2
            j = 1
            count = 0
            best_p, best_q = 0, 1  
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1
                if j == n:
                    break
                count += n - j
                if arr[i] * best_q > best_p * arr[j]:
                    best_p, best_q = arr[i], arr[j]
            if count == k:
                return [best_p, best_q]
            elif count < k:
                lo = mid
            else:
                hi = mid
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 5], 3, [2, 5]),
        ([1, 7], 1, [1, 7]),
        ([1, 2, 3, 5], 1, [1, 5]),
        ([1, 2, 3, 5], 6, [3, 5]),
    ]
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        result = sol.kthSmallestPrimeFraction(arr, k)
        status = "PASS" if result == expected else "FAIL"
        print("Test " + str(i) + ": arr=" + str(arr) + ", k=" + str(k) +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)