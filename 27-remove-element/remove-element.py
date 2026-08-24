class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_index = 0
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = sol.removeElement(nums, val)
    print(k, sorted(nums[:k]))  
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = sol.removeElement(nums, val)
    print(k, sorted(nums[:k]))  
    nums = []
    val = 5
    k = sol.removeElement(nums, val)
    print(k, nums[:k]) 
    nums = [1, 2, 3, 4]
    val = 10
    k = sol.removeElement(nums, val)
    print(k, sorted(nums[:k])) 
    nums = [5, 5, 5, 5]
    val = 5
    k = sol.removeElement(nums, val)
    print(k, nums[:k])  
    nums = [7]
    val = 7
    k = sol.removeElement(nums, val)
    print(k, nums[:k])  
    nums = [7]
    val = 3
    k = sol.removeElement(nums, val)
    print(k, nums[:k]) 
print(__name__)