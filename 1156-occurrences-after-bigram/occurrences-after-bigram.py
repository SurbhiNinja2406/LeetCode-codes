class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        result = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        return result
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("alice is a good girl she is a good student", "a", "good"),  
        ("we will we will rock you", "we", "will"),              
    ]
    for text, first, second in tests:
        print('text = "{}", first = "{}", second = "{}" -> {}'.format(
            text, first, second, sol.findOcurrences(text, first, second)))
print(__name__)