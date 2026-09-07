class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1 == s2:
            return 0
        def get_neighbors(s):
            neighbors = []
            i = 0
            while s[i] == s2[i]:
                i += 1
            s_list = list(s)
            for j in range(i + 1, len(s)):
                if s_list[j] == s2[i] and s_list[j] != s2[j]:
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    neighbors.append(''.join(s_list))
                    s_list[i], s_list[j] = s_list[j], s_list[i]  
            return neighbors
        visited = {s1}
        queue = [s1]
        steps = 0
        while queue:
            next_queue = []
            for current in queue:
                for neighbor in get_neighbors(current):
                    if neighbor == s2:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_queue.append(neighbor)
            queue = next_queue
            steps += 1
        return -1  
if __name__ == "__main__":
    solution = Solution()
    s1_1, s2_1 = "ab", "ba"
    print(solution.kSimilarity(s1_1, s2_1)) 
    s1_2, s2_2 = "abc", "bca"
    print(solution.kSimilarity(s1_2, s2_2))  
    s1_3, s2_3 = "abcd", "abcd"
    print(solution.kSimilarity(s1_3, s2_3))  
    s1_4, s2_4 = "abcdef", "fedcba"
    print(solution.kSimilarity(s1_4, s2_4))
    s1_5, s2_5 = "aabc", "abca"
    print(solution.kSimilarity(s1_5, s2_5))
    s1_6, s2_6 = "abcbadf", "acdbfba"
print(__name__)