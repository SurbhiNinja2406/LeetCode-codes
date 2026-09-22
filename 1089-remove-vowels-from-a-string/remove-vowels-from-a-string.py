class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return "".join(char for char in s if char not in vowels)
if __name__ == "__main__":
    solution = Solution()
    s1 = "leetcodeisacommunityforcoders"
    result1 = solution.removeVowels(s1)
    print("Example 1: '{}' (Expected: 'ltcdscmmntyfrcdrs')".format(result1))
    s2 = "aeiou"
    result2 = solution.removeVowels(s2)
    print("Example 2: '{}' (Expected: '')".format(result2))
print(__name__)