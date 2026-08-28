# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_map = {emp.id: emp for emp in employees}
        total = 0
        queue = [id]
        while queue:
            curr_id = queue.pop()
            emp = emp_map[curr_id]
            total += emp.importance
            queue.extend(emp.subordinates)
        return total
def build_employees(raw):
    return [Employee(e[0], e[1], e[2]) for e in raw]
if __name__ == "__main__":
    sol = Solution()
    employees1 = build_employees([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]])
    print(sol.getImportance(employees1, 1)) 
    employees2 = build_employees([[1, 2, [5]], [5, -3, []]])
    print(sol.getImportance(employees2, 5)) 
print(__name__)