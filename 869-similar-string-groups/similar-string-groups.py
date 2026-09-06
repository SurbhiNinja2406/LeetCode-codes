class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        parent = list(range(n))        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x       
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y        
        def is_similar(word1, word2):
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 2:
                        return False
            return True
        for i in range(n):
            for j in range(i + 1, n):
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    union(i, j)
        return len(set(find(i) for i in range(n)))
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSimilarGroups(["tars", "rats", "arts", "star"])) 
    print(sol.numSimilarGroups(["omv", "ovm"]))                   