from itertools import product

class Solution(object):
    def expand(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = s.index('}', i)               
                options = sorted(s[i + 1:j].split(','))   
                groups.append(options)
                i = j + 1
            else:
                groups.append([s[i]])                  
                i += 1
        return [''.join(combo) for combo in product(*groups)]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        "{a,b}c{d,e}f", 
        "abcd",       
    ]
    for t in tests:
        print('s = "{}" -> {}'.format(t, sol.expand(t)))
print(__name__)