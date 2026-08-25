class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}        
        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]                
                if word in word_set:
                    rest_sentences = backtrack(end)                    
                    for rest in rest_sentences:
                        if rest:
                            sentences.append(word + " " + rest)
                        else:
                            sentences.append(word)            
            memo[start] = sentences
            return sentences        
        return backtrack(0)
if __name__ == "__main__":
    sol = Solution()
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    print(sol.wordBreak(s1, wordDict1))
    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(sol.wordBreak(s2, wordDict2))
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s3, wordDict3))
print(__name__)