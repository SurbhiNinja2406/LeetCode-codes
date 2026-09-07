class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build_final_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack: 
                    stack.pop()
            return ''.join(stack)
        return build_final_string(s) == build_final_string(t)
if __name__ == "__main__":
    solution = Solution()
    s1, t1 = "ab#c", "ad#c"
    print(solution.backspaceCompare(s1, t1)) 
    s2, t2 = "ab##", "c#d#"
    print(solution.backspaceCompare(s2, t2)) 
    s3, t3 = "a#c", "b"
    print(solution.backspaceCompare(s3, t3))  
    s4, t4 = "####a", "#a#c"
    print(solution.backspaceCompare(s4, t4))  
    s5, t5 = "a##c", "#a#c"
    print(solution.backspaceCompare(s5, t5))  
    s6, t6 = "abc", "abc"
    print(solution.backspaceCompare(s6, t6)) 
print(__name__)