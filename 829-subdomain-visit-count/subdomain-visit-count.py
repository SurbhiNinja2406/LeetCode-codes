class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split(" ", 1)
            count = int(count_str)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] = counts.get(subdomain, 0) + count
        return ["{} {}".format(cnt, dom) for dom, cnt in counts.items()]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["9001 discuss.leetcode.com"],
         ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]),
        (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
         ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org",
          "5 org", "1 intel.mail.com", "951 com"]),
    ]
    for cpdomains, expected in test_cases:
        result = solution.subdomainVisits(list(cpdomains))
        result_set = set(result)
        expected_set = set(expected)
        status = "PASS" if result_set == expected_set else "FAIL"
        print("cpdomains={:<60} got={}".format(str(cpdomains), str(result)))
        print("  expected={} [{}]".format(str(expected), status))
print(__name__)