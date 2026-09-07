from collections import Counter
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diff_positions = [i for i in range(len(s)) if s[i] != goal[i]]
        if len(diff_positions) != 2:
            return False
        i, j = diff_positions
        return s[i] == goal[j] and s[j] == goal[i]
if __name__ == "__main__":
    solution = Solution()
    s1, goal1 = "ab", "ba"
    print(solution.buddyStrings(s1, goal1))  
    s2, goal2 = "ab", "ab"
    print(solution.buddyStrings(s2, goal2))  
    s3, goal3 = "aa", "aa"
    print(solution.buddyStrings(s3, goal3))  
    s4, goal4 = "abc", "ab"
    print(solution.buddyStrings(s4, goal4))  
    s5, goal5 = "abcd", "badc"
    print(solution.buddyStrings(s5, goal5)) 
    s6, goal6 = "abc", "abc"
    print(solution.buddyStrings(s6, goal6)) 
    s7, goal7 = "abc", "abd"
    print(solution.buddyStrings(s7, goal7))  
print(__name__)