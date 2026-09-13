class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        VOWELS = set('aeiou')        
        def devowel(word):
            return ''.join('*' if ch in VOWELS else ch for ch in word)        
        exact_set = set(wordlist)        
        case_insensitive_map = {}   
        devowel_map = {}       
        for word in wordlist:
            lower = word.lower()            
            if lower not in case_insensitive_map:
                case_insensitive_map[lower] = word            
            dv = devowel(lower)
            if dv not in devowel_map:
                devowel_map[dv] = word        
        result = []        
        for query in queries:
            if query in exact_set:
                result.append(query)
                continue            
            lower_query = query.lower()
            if lower_query in case_insensitive_map:
                result.append(case_insensitive_map[lower_query])
                continue            
            dv_query = devowel(lower_query)
            if dv_query in devowel_map:
                result.append(devowel_map[dv_query])
                continue
            result.append("")        
        return result
if __name__ == "__main__":
    sol = Solution()
    wordlist1 = ["KiTe", "kite", "hare", "Hare"]
    queries1 = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    result1 = sol.spellchecker(wordlist1, queries1)
    expected1 = ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
    print("Input: wordlist={}, queries={}".format(wordlist1, queries1))
    print("Output: {}".format(result1))
    print("Expected: {}".format(expected1))
    print("Pass: {}\n".format(result1 == expected1))
    wordlist2 = ["yellow"]
    queries2 = ["YellOw"]
    result2 = sol.spellchecker(wordlist2, queries2)
    expected2 = ["yellow"]
    print("Input: wordlist={}, queries={}".format(wordlist2, queries2))
    print("Output: {}".format(result2))
    print("Expected: {}".format(expected2))
    print("Pass: {}\n".format(result2 == expected2))
    wordlist3 = ["Yellow", "yellow"]
    queries3 = ["yellow"]
    result3 = sol.spellchecker(wordlist3, queries3)
    expected3 = ["yellow"]
    print("Input: wordlist={}, queries={}".format(wordlist3, queries3))
    print("Output: {}".format(result3))
    print("Expected: {}".format(expected3))
    print("Pass: {}\n".format(result3 == expected3))
    wordlist4 = ["apple", "banana"]
    queries4 = ["xyz"]
    result4 = sol.spellchecker(wordlist4, queries4)
    expected4 = [""]
    print("Input: wordlist={}, queries={}".format(wordlist4, queries4))
    print("Output: {}".format(result4))
    print("Expected: {}".format(expected4))
    print("Pass: {}\n".format(result4 == expected4))
    wordlist5 = ["star", "stir", "stur"]
    queries5 = ["stor"]
    result5 = sol.spellchecker(wordlist5, queries5)
    expected5 = ["star"]
    print("Input: wordlist={}, queries={}".format(wordlist5, queries5))
    print("Output: {}".format(result5))
    print("Expected: {}".format(expected5))
    print("Pass: {}\n".format(result5 == expected5))
print(__name__)