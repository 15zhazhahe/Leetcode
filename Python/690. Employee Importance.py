"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        maple = dict()
        for employee in employees:
            maple[employee.id] = employee
        def dfs(id):
            employee = maple[id]
            cnt = employee.importance
            for subordinate in employee.subordinates:
                cnt += dfs(subordinate)
            return cnt
        return dfs(id)