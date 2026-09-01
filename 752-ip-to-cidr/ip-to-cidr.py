class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        def ip_to_int(ip_str):
            parts = list(map(int, ip_str.split('.')))
            result = 0
            for part in parts:
                result = (result << 8) | part
            return result
        def int_to_ip(num):
            return ".".join(str((num >> shift) & 255) for shift in [24, 16, 8, 0])
        start = ip_to_int(ip)
        result = []
        while n > 0:
            if start == 0:
                max_block_by_alignment = 1 << 32  
            else:
                max_block_by_alignment = start & (-start)
            max_block_by_remaining = 1
            while max_block_by_remaining * 2 <= n:
                max_block_by_remaining *= 2
            block_size = min(max_block_by_alignment, max_block_by_remaining)
            prefix_length = 32 - block_size.bit_length() + 1
            result.append(int_to_ip(start) + "/" + str(prefix_length))
            start += block_size
            n -= block_size
        return result
if __name__ == "__main__":
    solution = Solution()
    ip1 = "255.0.0.7"
    n1 = 10
    result1 = solution.ipToCIDR(ip1, n1)
    expected1 = ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]
    print("Example 1: Output = {0}".format(result1))
    print("Expected = {0}".format(expected1))
    assert result1 == expected1
    ip2 = "117.145.102.62"
    n2 = 8
    result2 = solution.ipToCIDR(ip2, n2)
    expected2 = ["117.145.102.62/31", "117.145.102.64/30", "117.145.102.68/31"]
    print("Example 2: Output = {0}".format(result2))
    print("Expected = {0}".format(expected2))
    assert result2 == expected2
    print("\nAll test cases passed!")
print(__name__)