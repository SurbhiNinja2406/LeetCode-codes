class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            digit1 = int(num1[i])            
            for j in range(n - 1, -1, -1):
                digit2 = int(num2[j])
                mul = digit1 * digit2
                pos_low = i + j + 1
                pos_high = i + j
                total = mul + result[pos_low]                
                result[pos_low] = total % 10
                result[pos_high] += total // 10
        result_str = "".join(map(str, result))
        result_str = result_str.lstrip("0")        
        return result_str if result_str else "0"
if __name__ == "__main__":
    solution = Solution()
    num1_1, num2_1 = "2", "3"
    print(solution.multiply(num1_1, num2_1))  
    num1_2, num2_2 = "123", "456"
    print(solution.multiply(num1_2, num2_2)) 
print(__name__)