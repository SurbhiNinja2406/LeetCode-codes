class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = {}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)
        groups = {}
        for email in parent:
            root = find(email)
            groups.setdefault(root, []).append(email)
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))
        return result
if __name__ == "__main__":
    sol = Solution()
    def normalize(result):
        """Sort each account's emails (already sorted by solution) and
        sort the list of accounts themselves, so comparisons are
        order-independent (as the problem allows any output order)."""
        return sorted([acc[0]] + sorted(acc[1:]) for acc in result)
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    result1 = sol.accountsMerge(accounts1)
    expected1 = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    print("Example 1 output:", result1)
    print("Example 1 match:", normalize(result1) == normalize(expected1))
    print()
    accounts2 = [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
    ]
    result2 = sol.accountsMerge(accounts2)
    expected2 = [
        ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]
    ]
    print("Example 2 output:", result2)
    print("Example 2 match:", normalize(result2) == normalize(expected2))
    print()
    accounts3 = [
        ["Alex", "alex1@mail.com"],
        ["Alex", "alex2@mail.com"]
    ]
    result3 = sol.accountsMerge(accounts3)
    print("Extra test (same name, different people):", result3)
    print("Should remain 2 separate accounts:", len(result3) == 2)
    print()
    accounts4 = [
        ["A", "a1@mail.com", "a2@mail.com"],
        ["A", "a2@mail.com", "a3@mail.com"],
        ["A", "a3@mail.com", "a4@mail.com"]
    ]
    result4 = sol.accountsMerge(accounts4)
    print("Extra test (chain merge):", result4)
    print("Should merge into 1 account with 4 emails:",
          len(result4) == 1 and len(result4[0]) == 5)
print(__name__)