class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k]) 
    nums = [5]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  
    nums = [7, 7, 7, 7]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k]) 
    nums = [1, 2, 3, 4, 5]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])
    nums = [-3, -3, -1, 0, 0, 0, 2]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k]) 
print(__name__)