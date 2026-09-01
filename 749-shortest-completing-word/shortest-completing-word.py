from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        required = Counter()
        for ch in licensePlate.lower():
            if ch.isalpha():
                required[ch] += 1
        best = None
        for word in words:
            word_count = Counter(word) 
            if all(word_count[letter] >= count for letter, count in required.items()):
                if best is None or len(word) < len(best):
                    best = word
        return best
if __name__ == "__main__":
    solution = Solution()
    licensePlate1 = "1s3 PSt"
    words1 = ["step", "steps", "stripe", "stepple"]
    result1 = solution.shortestCompletingWord(licensePlate1, words1)
    print("Example 1: Output = {0}, Expected = steps".format(result1))
    assert result1 == "steps"
    licensePlate2 = "1s3 456"
    words2 = ["looks", "pest", "stew", "show"]
    result2 = solution.shortestCompletingWord(licensePlate2, words2)
    print("Example 2: Output = {0}, Expected = pest".format(result2))
    assert result2 == "pest"
    print("\nAll test cases passed!")
print(__name__)