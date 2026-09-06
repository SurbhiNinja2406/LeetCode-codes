class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        at_index = s.find('@')
        if at_index != -1:
            name = s[:at_index]
            domain = s[at_index + 1:]            
            name = name.lower()
            domain = domain.lower()            
            masked_name = name[0] + "*****" + name[-1]            
            return masked_name + "@" + domain        
        else:
            digits = ''.join(ch for ch in s if ch.isdigit())            
            n = len(digits)
            local_number = digits[-10:]
            country_code = digits[:-10]  
            local_masked = "***-***-" + local_number[-4:]            
            country_len = len(country_code)
            if country_len == 0:
                return local_masked
            else:
                return "+" + "*" * country_len + "-" + local_masked
if __name__ == "__main__":
    sol = Solution()
    print(sol.maskPII("LeetCode@LeetCode.com"))  
    print(sol.maskPII("AB@qq.com"))         
    print(sol.maskPII("1(234)567-890"))     
print(__name__)