from collections import Counter

class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        unique_nums = [num for num, cnt in counts.items() if cnt == 1]
        return max(unique_nums) if unique_nums else -1
if __name__ == "__main__":
    sol = Solution()
    nums1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    print(sol.largestUniqueNumber(nums1))  
    nums2 = [9, 9, 8, 8]
    print(sol.largestUniqueNumber(nums2)) 
print(__name__)