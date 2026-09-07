class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        n = len(num)
        result = []
        def backtrack(index, sequence):
            if index == n:
                return len(sequence) >= 3
            for length in range(1, n - index + 1):
                if num[index] == '0' and length > 1:
                    break
                piece_str = num[index:index + length]
                piece = int(piece_str)
                if piece > 2**31 - 1:
                    break
                if len(sequence) >= 2:
                    if piece < sequence[-1] + sequence[-2]:
                        continue
                    elif piece > sequence[-1] + sequence[-2]:
                        break
                sequence.append(piece)
                if backtrack(index + length, sequence):
                    return True
                sequence.pop()
            return False
        if backtrack(0, result):
            return result
        return []
if __name__ == "__main__":
    solution = Solution()
    num1 = "1101111"
    print(solution.splitIntoFibonacci(num1))  
    num2 = "112358130"
    print(solution.splitIntoFibonacci(num2)) 
    num3 = "0123"
    print(solution.splitIntoFibonacci(num3))  
    num4 = "123456579"
    print(solution.splitIntoFibonacci(num4)) 
    num5 = "000"
    print(solution.splitIntoFibonacci(num5))  
print(__name__)