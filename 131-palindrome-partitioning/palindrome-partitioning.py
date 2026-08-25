class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        current_partition = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]        
        def backtrack(start):
            if start == len(s):
                result.append(current_partition[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]                
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(end)
                    current_partition.pop()        
        backtrack(0)
        return result
if __name__ == "__main__":
    sol = Solution()
    s1 = "aab"
    print(sol.partition(s1))  
    s2 = "a"
    print(sol.partition(s2)) 
print(__name__)