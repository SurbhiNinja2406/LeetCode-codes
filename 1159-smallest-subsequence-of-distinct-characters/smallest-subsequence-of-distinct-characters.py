class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        in_stack = set()
        for i, ch in enumerate(s):
            if ch in in_stack:
                continue  
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)
if __name__ == "__main__":
    sol = Solution()
    tests = [
        "bcabc",    
        "cbacdcbc",  
    ]
    for t in tests:
        print('s = "{}" -> "{}"'.format(t, sol.smallestSubsequence(t)))
print(__name__)