class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        in_block_comment = False
        current_line = []
        for line in source:
            i = 0
            n = len(line)
            if not in_block_comment:
                current_line = []
            while i < n:
                if in_block_comment:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        in_block_comment = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        in_block_comment = True
                        i += 2
                    else:
                        current_line.append(line[i])
                        i += 1
            if not in_block_comment:
                if current_line:
                    result.append("".join(current_line))
        return result
if __name__ == "__main__":
    sol = Solution()
    source1 = [
        "/*Test program */", "int main()", "{ ", "  // variable declaration ",
        "int a, b, c;", "/* This is a test",
        "   multiline", "   comment for ",
        "   testing */", "a = b + c;", "}"
    ]
    result1 = sol.removeComments(source1)
    expected1 = ["int main()", "{ ", "", "int a, b, c;", "a = b + c;", "}"]
    print("Example 1 output:", result1)
    print("Example 1 expected:", expected1)
    print("Match:", result1 == expected1)
    print()
    source2 = ["a/*comment", "line", "more_comment*/b"]
    result2 = sol.removeComments(source2)
    expected2 = ["ab"]
    print("Example 2 output:", result2)
    print("Example 2 expected:", expected2)
    print("Match:", result2 == expected2)
    print()
    source3 = ["int x = 5;", "int y = 10;"]
    result3 = sol.removeComments(source3)
    print("Extra test (no comments) output:", result3)
    print("Expected:", source3)
    print()
    source4 = ["// just a comment", "int x = 1;"]
    result4 = sol.removeComments(source4)
    print("Extra test (full-line comment) output:", result4)
    print("Expected:", ["int x = 1;"])
    print()
    source5 = ["/*", "comment", "spans", "lines", "*/", "code_after;"]
    result5 = sol.removeComments(source5)
    print("Extra test (multi-line block) output:", result5)
    print("Expected:", ["code_after;"])
print(__name__)