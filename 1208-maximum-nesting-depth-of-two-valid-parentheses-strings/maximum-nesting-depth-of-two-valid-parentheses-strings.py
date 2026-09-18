class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        answer = [0] * len(seq)
        depth = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                depth += 1
                answer[i] = 1 - (depth % 2)
            else: 
                answer[i] = 1 - (depth % 2)
                depth -= 1
        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepthAfterSplit("(()())")) 
    print(sol.maxDepthAfterSplit("()(())()"))   
print(__name__)