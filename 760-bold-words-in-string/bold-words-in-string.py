class Solution(object):
    def boldWords(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: str
        """
        n = len(s)
        bold = [False] * n
        for word in words:
            wl = len(word)
            if wl == 0:
                continue
            start = 0
            while True:
                idx = s.find(word, start)
                if idx == -1:
                    break
                for i in range(idx, idx + wl):
                    bold[i] = True
                start = idx + 1  
        result = []
        i = 0
        while i < n:
            if bold[i]:
                j = i
                while j < n and bold[j]:
                    j += 1
                result.append("<b>")
                result.append(s[i:j])
                result.append("</b>")
                i = j
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.boldWords(["ab", "bc"], "aabcd"))
    print(sol.boldWords(["ab", "cb"], "aabcd"))
print(__name__)