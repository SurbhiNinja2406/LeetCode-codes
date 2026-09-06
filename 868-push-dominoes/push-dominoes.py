class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        s = 'L' + dominoes + 'R'        
        result = list(s)
        prev_index = 0      
        prev_char = 'L'     
        for i in range(1, len(s)):
            curr_char = s[i]            
            if curr_char == '.':
                continue  
            if prev_char == curr_char:
                for j in range(prev_index + 1, i):
                    result[j] = curr_char
            elif prev_char == 'R' and curr_char == 'L':
                left, right = prev_index + 1, i - 1
                while left < right:
                    result[left] = 'R'
                    result[right] = 'L'
                    left += 1
                    right -= 1
            prev_index = i
            prev_char = curr_char
        return ''.join(result[1:-1])
if __name__ == "__main__":
    sol = Solution()
    print(sol.pushDominoes("RR.L"))             
    print(sol.pushDominoes(".L.R...LR..L.."))       
print(__name__)