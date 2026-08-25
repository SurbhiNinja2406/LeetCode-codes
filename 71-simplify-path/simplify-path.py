class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        components = path.split('/')        
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)        
        return '/' + '/'.join(stack)
if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home/")) 
    print(sol.simplifyPath("/home//foo/"))  
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))  
    print(sol.simplifyPath("/../")) 
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))  
print(__name__)