from collections import deque
class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}
        self.max_len = 0
        for word in words:
            node = self.root
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node['#'] = True      
            self.max_len = max(self.max_len, len(word))
        self.stream = deque(maxlen=self.max_len)
    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream):
            if ch not in node:
                return False
            node = node[ch]
            if '#' in node:        
                return True
        return False
if __name__ == "__main__":
    checker = StreamChecker(["cd", "f", "kl"])
    letters = "abcdefghijkl"
    expected = [False, False, False, True, False, True,
                False, False, False, False, False, True]
    for ch, exp in zip(letters, expected):
        result = checker.query(ch)
        status = "PASS" if result == exp else "FAIL"
        print("{}: query('{}') -> {}, expected {}".format(status, ch, result, exp))
print(__name__)
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)