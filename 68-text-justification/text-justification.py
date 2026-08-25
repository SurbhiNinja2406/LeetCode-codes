class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        current_line = []
        current_length = 0
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                result.append(self._justify_line(current_line, current_length, maxWidth))
                current_line = []
                current_length = 0
            current_line.append(word)
            current_length += len(word)
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        return result
    def _justify_line(self, words, total_word_length, maxWidth):
        if len(words) == 1:
            return words[0] + ' ' * (maxWidth - total_word_length)
        total_spaces = maxWidth - total_word_length
        gaps = len(words) - 1
        space_each = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        line = ""
        for i in range(gaps):
            line += words[i]
            spaces_to_add = space_each + (1 if i < extra_spaces else 0)
            line += ' ' * spaces_to_add
        line += words[-1]
        return line
if __name__ == "__main__":
    sol = Solution()
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    print(sol.fullJustify(words1, 16))
    words2 = ["What","must","be","acknowledgment","shall","be"]
    print(sol.fullJustify(words2, 16))
    words3 = ["Science","is","what","we","understand","well","enough","to","explain",
               "to","a","computer.","Art","is","everything","else","we","do"]
    print(sol.fullJustify(words3, 20))
print(__name__)