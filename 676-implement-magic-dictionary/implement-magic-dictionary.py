from collections import defaultdict
class MagicDictionary(object):
    def __init__(self):
        self.words_by_length = defaultdict(list)
    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            self.words_by_length[len(word)].append(word)
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        candidates = self.words_by_length.get(len(searchWord), [])
        for word in candidates:
            diff_count = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        break 
            if diff_count == 1:
                return True
        return False
if __name__ == "__main__":
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello", "leetcode"])
    r1 = magicDictionary.search("hello")
    print("search('hello'):", r1, "| Expected: False")
    r2 = magicDictionary.search("hhllo")
    print("search('hhllo'):", r2, "| Expected: True")
    r3 = magicDictionary.search("hell")
    print("search('hell'):", r3, "| Expected: False")
    r4 = magicDictionary.search("leetcoded")
    print("search('leetcoded'):", r4, "| Expected: False")
    print()
    md2 = MagicDictionary()
    md2.buildDict(["hello", "hallo", "leetcode"])
    r5 = md2.search("hello")
    print("search('hello') [multi-candidate]:", r5, "| Expected: True")
    r6 = md2.search("xxxxx")
    print("search('xxxxx') [no match]:", r6, "| Expected: False")
    r7 = md2.search("z")
    print("search('z') [no same-length words]:", r7, "| Expected: False")
print(__name__)
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)