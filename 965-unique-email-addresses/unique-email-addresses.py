class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@', 1)
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numUniqueEmails([
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]))
    print(sol.numUniqueEmails([
        "a@leetcode.com",
        "b@leetcode.com",
        "c@leetcode.com"
    ]))
print(__name__)