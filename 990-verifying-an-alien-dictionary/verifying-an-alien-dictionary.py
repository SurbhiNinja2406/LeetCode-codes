class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        rank = {}
        for i, ch in enumerate(order):
            rank[ch] = i        
        def in_order(w1, w2):
            min_len = min(len(w1), len(w2))
            for i in range(min_len):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    return rank[c1] < rank[c2]
            return len(w1) <= len(w2)        
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False        
        return True
if __name__ == "__main__":
    sol = Solution()
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    result1 = sol.isAlienSorted(words1, order1)
    print("Input: words={}, order={}".format(words1, order1))
    print("Output: {}".format(result1))
    print("Expected: True")
    print("Pass: {}\n".format(result1 == True))
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    result2 = sol.isAlienSorted(words2, order2)
    print("Input: words={}, order={}".format(words2, order2))
    print("Output: {}".format(result2))
    print("Expected: False")
    print("Pass: {}\n".format(result2 == False))
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    result3 = sol.isAlienSorted(words3, order3)
    print("Input: words={}, order={}".format(words3, order3))
    print("Output: {}".format(result3))
    print("Expected: False")
    print("Pass: {}\n".format(result3 == False))
    words4 = ["single"]
    order4 = "abcdefghijklmnopqrstuvwxyz"
    result4 = sol.isAlienSorted(words4, order4)
    print("Input: words={}, order={}".format(words4, order4))
    print("Output: {}".format(result4))
    print("Expected: True")
    print("Pass: {}\n".format(result4 == True))
    words5 = ["same", "same"]
    order5 = "abcdefghijklmnopqrstuvwxyz"
    result5 = sol.isAlienSorted(words5, order5)
    print("Input: words={}, order={}".format(words5, order5))
    print("Output: {}".format(result5))
    print("Expected: True")
    print("Pass: {}\n".format(result5 == True))
print(__name__)