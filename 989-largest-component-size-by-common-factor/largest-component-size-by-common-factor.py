class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_val = max(nums)
        parent = list(range(n + max_val + 1))
        size = [1] * (n + max_val + 1)        
        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]        
        def prime_factors(num):
            factors = []
            d = 2
            while d * d <= num:
                if num % d == 0:
                    factors.append(d)
                    while num % d == 0:
                        num //= d
                d += 1
            if num > 1:
                factors.append(num)
            return factors
        for i, num in enumerate(nums):
            for p in prime_factors(num):
                union(i, n + p)
        from collections import defaultdict
        count = defaultdict(int)
        best = 0
        for i in range(n):
            root = find(i)
            count[root] += 1
            best = max(best, count[root])
        return best
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 6, 15, 35]
    result1 = sol.largestComponentSize(nums1)
    print("Input: {}".format(nums1))
    print("Output: {}".format(result1))
    print("Expected: 4")
    print("Pass: {}\n".format(result1 == 4))
    nums2 = [20, 50, 9, 63]
    result2 = sol.largestComponentSize(nums2)
    print("Input: {}".format(nums2))
    print("Output: {}".format(result2))
    print("Expected: 2")
    print("Pass: {}\n".format(result2 == 2))
    nums3 = [2, 3, 6, 7, 4, 12, 21, 39]
    result3 = sol.largestComponentSize(nums3)
    print("Input: {}".format(nums3))
    print("Output: {}".format(result3))
    print("Expected: 8")
    print("Pass: {}\n".format(result3 == 8))
    nums4 = [1]
    result4 = sol.largestComponentSize(nums4)
    print("Input: {}".format(nums4))
    print("Output: {}".format(result4))
    print("Expected: 1")
    print("Pass: {}\n".format(result4 == 1))
    nums5 = [2, 3, 5, 7, 11]
    result5 = sol.largestComponentSize(nums5)
    print("Input: {}".format(nums5))
    print("Output: {}".format(result5))
    print("Expected: 1")
    print("Pass: {}\n".format(result5 == 1))
print(__name__)