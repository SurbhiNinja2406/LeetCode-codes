class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = [""]
        for ch in s:
            if ch.isalpha():
                new_results = []
                for prefix in results:
                    new_results.append(prefix + ch.lower())
                    new_results.append(prefix + ch.upper())
                results = new_results
            else:
                results = [prefix + ch for prefix in results]
        return results
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]),
        ("3z4", ["3z4", "3Z4"]),
    ]
    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.letterCasePermutation(s)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print("Test " + str(i) + ": s=" + s +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)