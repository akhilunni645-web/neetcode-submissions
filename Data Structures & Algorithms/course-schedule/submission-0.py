class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Step 1: Build adjacency list
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        # Step 2: Current DFS path
        path = set()

        # Step 3: DFS function
        def dfs(course):

            # Cycle detected
            if course in path:
                return False

            # No prerequisites
            if preMap[course] == []:
                return True

            # Add current course to recursion stack
            path.add(course)

            # Visit prerequisites
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            # Remove after DFS finishes
            path.remove(course)

            # Memoization
            preMap[course] = []

            return True

        # Step 4: Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True