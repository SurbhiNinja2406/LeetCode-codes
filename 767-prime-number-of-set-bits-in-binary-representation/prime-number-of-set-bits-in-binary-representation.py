class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in primes:
                count += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    left, right = 6, 10
    print("Input: left = {}, right = {}".format(left, right))
    print("Output: {}".format(sol.countPrimeSetBits(left, right)))
    print("Expected: 4\n")
    left, right = 10, 15
    print("Input: left = {}, right = {}".format(left, right))
    print("Output: {}".format(sol.countPrimeSetBits(left, right)))
    print("Expected: 5\n")
    left, right = 1, 1
    print("Input: left = {}, right = {}".format(left, right))
    print("Output: {}".format(sol.countPrimeSetBits(left, right)))
print(__name__)