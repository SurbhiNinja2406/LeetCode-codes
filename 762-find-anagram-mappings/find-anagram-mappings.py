from collections import defaultdict
class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        value_to_indices = defaultdict(list)
        for idx, val in enumerate(nums2):
            value_to_indices[val].append(idx)
        mapping = []
        for val in nums1:
            mapping.append(value_to_indices[val].pop())
        return mapping
if __name__ == "__main__":
    sol = Solution()
    print(sol.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
    print(sol.anagramMappings([84, 46], [84, 46]))
print(__name__)