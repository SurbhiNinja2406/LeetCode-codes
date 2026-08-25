class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1                
                longest = max(longest, current_length)        
        return longest
if __name__ == "__main__":
    sol = Solution()
    nums1 = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums1)) 
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longestConsecutive(nums2)) 
    nums3 = [1, 0, 1, 2]
    print(sol.longestConsecutive(nums3)) 
print(__name__)