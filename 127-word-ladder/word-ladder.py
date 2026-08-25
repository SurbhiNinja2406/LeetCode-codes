from collections import deque
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)        
        if endWord not in word_set:
            return 0        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}        
        while queue:
            word, length = queue.popleft()            
            if word == endWord:
                return length            
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
                    next_word = word[:i] + c + word[i + 1:]                    
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))        
        return 0
if __name__ == "__main__":
    sol = Solution()
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord1, endWord1, wordList1)) 
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print(sol.ladderLength(beginWord2, endWord2, wordList2))  