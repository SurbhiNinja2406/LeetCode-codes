class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        words = sentence.split(' ')
        result = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            new_word += "a" * (i + 1)
            result.append(new_word)
        return ' '.join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.toGoatLatin("I speak Goat Latin"))
    print(sol.toGoatLatin("The quick brown fox jumped over the lazy dog"))
print(__name__)