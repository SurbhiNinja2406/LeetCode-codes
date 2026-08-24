class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        if s_len < total_len:
            return []
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        result = []
        for offset in range(word_len):
            left = offset
            count = 0
            window_count = {}
            for right in range(offset, s_len - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word in word_count:
                    window_count[word] = window_count.get(word, 0) + 1
                    count += 1
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    window_count = {}
                    count = 0
                    left = right + word_len
        return result