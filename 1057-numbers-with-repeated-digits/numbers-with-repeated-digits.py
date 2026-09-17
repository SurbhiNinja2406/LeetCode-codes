class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        def perm(available, choose):
            if choose < 0 or choose > available:
                return 0
            result = 1
            for i in range(choose):
                result *= (available - i)
            return result
        digits = list(map(int, str(n)))
        L = len(digits)
        unique_count = 0
        for length in range(1, L):
            unique_count += 9 * perm(9, length - 1)
        used = set()
        for i, d in enumerate(digits):
            start = 1 if i == 0 else 0
            for x in range(start, d):
                if x in used:
                    continue
                remaining = L - i - 1
                available = 9 - len(used)
                unique_count += perm(available, remaining)
            if d in used:
                break
            used.add(d)
        else:
            unique_count += 1
        return n - unique_count
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (20, 1),
        (100, 10),
        (1000, 262),
        (9, 0),
        (11, 1),
    ]
    for n, expected in test_cases:
        result = sol.numDupDigitsAtMostN(n)
        status = "PASS" if result == expected else "FAIL"
        print("n={0} -> {1} (expected {2}) [{3}]".format(
            n, result, expected, status
        ))