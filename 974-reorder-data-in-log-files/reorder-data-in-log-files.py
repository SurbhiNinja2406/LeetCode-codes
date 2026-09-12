class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def get_key(log):
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                return (1,)
            else:
                return (0, rest, identifier)
        return sorted(logs, key=get_key)
if __name__ == "__main__":
    sol = Solution()
    logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(sol.reorderLogFiles(logs1))
    logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(sol.reorderLogFiles(logs2))
print(__name__)