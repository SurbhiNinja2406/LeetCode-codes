from collections import deque, defaultdict

class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)  
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
        semesters = 0
        courses_taken = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                courses_taken += 1
                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
        return semesters if courses_taken == n else -1
if __name__ == "__main__":
    sol = Solution()
    n1 = 3
    relations1 = [[1, 3], [2, 3]]
    print(sol.minimumSemesters(n1, relations1)) 
    n2 = 3
    relations2 = [[1, 2], [2, 3], [3, 1]]
    print(sol.minimumSemesters(n2, relations2)) 
print(__name__)