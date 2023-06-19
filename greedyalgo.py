import numpy as np
from itertools import product

class GreedyAlgorithm:
    def __init__(self, data, func):
        self.data = data
        self.bounds = []
        self.objective_function = func
        self.constraints = []
        
    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        
    def add_bound(self, _min, _max):
        self.bounds.append((_min, _max))
        
    def set_bounds(self, bounds):
        self.bounds = bounds
        
    def generate_random_solution_space(self):
        self.data = list(product(*(range(low, high+1) for low, high in self.bounds)))   #[[i] for i in range(bounds[j][0], bounds[j][1]) for j in range(0, n)]
        return self.data
        
    def search_optimum(self):
        valid_solutions = []
        
        for solution in self.data:
            is_valid = True
            for constraint in self.constraints:
                is_valid = is_valid and constraint(solution)
            if is_valid:
                valid_solutions.append(solution)

        # Find the best solution
        best_solution = min(valid_solutions, key=self.objective_function)
        return best_solution

# Define the objective function and constraints
# def objective_function(params):
    # return -params[0]**2 + params[1]**2 + params[2]**2

# def constraint_1(params):
    # return sum(params) >= 0

# def constraint_2(params):
    # return params[0] - params[1] >= 0

# def constraint_3(params):
    # return all(element <= 10 for element in params)

# Generate all possible solutions
# (min0, max0) = (0, 10)
# (min1, max1) = (0, 9)
# (min2, max2) = (0, 7)

# bounds = [(min0, max0), (min1, max1), (min2, max2)]  # Define the ranges for each element
# greedyAlgo = GreedyAlgorithm(None, objective_function)
# greedyAlgo.set_bounds(bounds)
# greedyAlgo.add_constraint(constraint_1)
# greedyAlgo.add_constraint(constraint_2)
# greedyAlgo.add_constraint(constraint_3)
# greedyAlgo.generate_random_solution_space()
# print(greedyAlgo.search_optimum())