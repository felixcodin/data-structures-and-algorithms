import unittest
from find_all_possible_recipes_from_given_supplies import Solution

class TestFindAllRecipes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["yeast", "flour", "corn"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["bread"])

    def testExampleCase2(self):
        recipes = ["bread", "sandwich"]
        ingredients = [["yeast", "flour"], ["bread", "meat"]]
        supplies = ["yeast", "flour", "meat"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["bread", "sandwich"])

    def testExampleCase3(self):
        recipes = ["bread", "sandwich", "burger"]
        ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
        supplies = ["yeast", "flour", "meat"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["bread", "burger", "sandwich"])

    def testNoRecipesPossible(self):
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["meat"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(res, [])

    def testAllSuppliesAvailable(self):
        recipes = ["salad", "soup"]
        ingredients = [["lettuce", "tomato"], ["carrot", "water"]]
        supplies = ["lettuce", "tomato", "carrot", "water"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["salad", "soup"])

    def testEmptyRecipes(self):
        recipes = []
        ingredients = []
        supplies = ["yeast", "flour"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(res, [])

    def testCircularDependency(self):
        recipes = ["bread", "sandwich"]
        ingredients = [["sandwich"], ["bread"]]
        supplies = []
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(res, [])

    def testChainedRecipes(self):
        recipes = ["a", "b", "c"]
        ingredients = [["x"], ["a"], ["b"]]
        supplies = ["x"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["a", "b", "c"])

    def testPartialChain(self):
        recipes = ["a", "b", "c"]
        ingredients = [["x"], ["a"], ["y"]]
        supplies = ["x"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["a", "b"])

    def testRecipeUsedMultipleTimes(self):
        recipes = ["a", "b", "c"]
        ingredients = [["x"], ["a"], ["a"]]
        supplies = ["x"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["a", "b", "c"])

    def testComplexDependencies(self):
        recipes = ["a", "b", "c", "d"]
        ingredients = [["x", "y"], ["a"], ["a", "b"], ["c"]]
        supplies = ["x", "y"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["a", "b", "c", "d"])

    def testMissingOneIngredient(self):
        recipes = ["bread", "sandwich"]
        ingredients = [["yeast", "flour"], ["bread", "meat", "cheese"]]
        supplies = ["yeast", "flour", "meat"]
        res = self.solution.findAllRecipes(recipes, ingredients, supplies)
        self.assertEqual(sorted(res), ["bread"])

if __name__ == '__main__':
    unittest.main()