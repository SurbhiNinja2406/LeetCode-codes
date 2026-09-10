from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = defaultdict(int)  
        left = 0
        max_fruits = 0
        for right, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
if __name__ == "__main__":
    solution = Solution()
    fruits1 = [1, 2, 1]
    print("Example 1:")
    print("Input: fruits =", fruits1)
    print("Output:", solution.totalFruit(fruits1))
    print()
    fruits2 = [0, 1, 2, 2]
    print("Example 2:")
    print("Input: fruits =", fruits2)
    print("Output:", solution.totalFruit(fruits2))
    print()
    fruits3 = [1, 2, 3, 2, 2]
    print("Example 3:")
    print("Input: fruits =", fruits3)
    print("Output:", solution.totalFruit(fruits3))
print(__name__)