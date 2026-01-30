import unittest
from course_schedule import Solution

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testNoCourses(self):
        numCourses = 0
        prerequisites = []
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testSingleCourse(self):
        numCourses = 1
        prerequisites = []
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testNoPrerequisites(self):
        numCourses = 5
        prerequisites = []
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testSimpleValid(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testSimpleCycle(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertFalse(result)

    def testLinearChain(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testMultiplePaths(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testCycleInMiddle(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [1, 2], [3, 2]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertFalse(result)

    def testSelfLoop(self):
        numCourses = 2
        prerequisites = [[0, 0]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertFalse(result)

    def testDisconnectedGraph(self):
        numCourses = 5
        prerequisites = [[1, 0], [3, 2]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)

    def testLargeCycle(self):
        numCourses = 5
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertFalse(result)

    def testComplexValid(self):
        numCourses = 6
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]]
        result = self.solution.canFinish(numCourses, prerequisites)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()