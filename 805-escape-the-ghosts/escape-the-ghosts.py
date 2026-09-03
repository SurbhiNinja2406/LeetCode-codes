class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_distance = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            ghost_distance = abs(target[0] - gx) + abs(target[1] - gy)
            if ghost_distance <= my_distance:
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    print(sol.escapeGhosts([[1,0],[0,3]], [0,1]))  
    print(sol.escapeGhosts([[1,0]], [2,0]))      
    print(sol.escapeGhosts([[2,0]], [1,0]))    
print(__name__)