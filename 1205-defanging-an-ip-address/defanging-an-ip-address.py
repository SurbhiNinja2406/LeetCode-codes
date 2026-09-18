class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')
if __name__ == "__main__":
    sol = Solution()
    print(sol.defangIPaddr("1.1.1.1")) 
    print(sol.defangIPaddr("255.100.50.0"))  