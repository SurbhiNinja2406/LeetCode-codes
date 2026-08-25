from collections import defaultdict, deque
import string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        result = []
        if endWord not in word_set:
            return result
        parents = defaultdict(set)
        current_level = {beginWord}
        word_set.discard(beginWord)
        found = False        
        while current_level and not found:
            for word in current_level:
                word_set.discard(word)            
            next_level = defaultdict(set)            
            for word in current_level:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i + 1:]                        
                        if next_word in word_set:
                            next_level[next_word].add(word)
                            if next_word == endWord:
                                found = True
            for word, preds in next_level.items():
                parents[word] |= preds            
            current_level = set(next_level.keys())        
        if not found:
            return result
        path = [endWord]
        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()        
        backtrack(endWord)        
        return result
if __name__ == "__main__":
    sol = Solution()
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.findLadders(beginWord1, endWord1, wordList1))
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print(sol.findLadders(beginWord2, endWord2, wordList2))
print(__name__)