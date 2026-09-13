class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 3]
    result1 = sol.repeatedNTimes(nums1)
    print("Input: {}".format(nums1))
    print("Output: {}".format(result1))
    print("Expected: 3")
    print("Pass: {}\n".format(result1 == 3))
    nums2 = [2, 1, 2, 5, 3, 2]
    result2 = sol.repeatedNTimes(nums2)
    print("Input: {}".format(nums2))
    print("Output: {}".format(result2))
    print("Expected: 2")
    print("Pass: {}\n".format(result2 == 2))
    nums3 = [5, 1, 5, 2, 5, 3, 5, 4]
    result3 = sol.repeatedNTimes(nums3)
    print("Input: {}".format(nums3))
    print("Output: {}".format(result3))
    print("Expected: 5")
    print("Pass: {}\n".format(result3 == 5))
    nums4 = [1, 2, 3, 1]
    result4 = sol.repeatedNTimes(nums4)
    print("Input: {}".format(nums4))
    print("Output: {}".format(result4))
    print("Expected: 1")
    print("Pass: {}\n".format(result4 == 1))
    nums5 = [0, 1, 0, 2]
    result5 = sol.repeatedNTimes(nums5)
    print("Input: {}".format(nums5))
    print("Output: {}".format(result5))
    print("Expected: 0")
    print("Pass: {}\n".format(result5 == 0))
    nums6 = [1, 1, 2, 3]
    result6 = sol.repeatedNTimes(nums6)
    print("Input: {}".format(nums6))
    print("Output: {}".format(result6))
    print("Expected: 1")
    print("Pass: {}\n".format(result6 == 1))
print(__name__)