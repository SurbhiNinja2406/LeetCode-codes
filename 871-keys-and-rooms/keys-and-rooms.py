class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        return all(visited)
if __name__ == "__main__":
    solution = Solution()
    rooms1 = [[1], [2], [3], []]
    print(solution.canVisitAllRooms(rooms1)) 
    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    print(solution.canVisitAllRooms(rooms2))  
    rooms3 = [[]]
    print(solution.canVisitAllRooms(rooms3))  
    rooms4 = [[1], [2], [0], []]
    print(solution.canVisitAllRooms(rooms4)) 
print(__name__)