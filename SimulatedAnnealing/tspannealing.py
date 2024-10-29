import mlrose_hiive as mlrose
import numpy as np
from scipy.spatial.distance import euclidean

# Define the coordinates of the cities
coords = [(0, 0), (1, 5), (2, 3), (5, 1), (6, 4), (7, 2)]

# Calculate the distances between each pair of cities
distances = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        dist = euclidean(coords[i], coords[j])
        distances.append((i, j, dist))

# Create a fitness function for the TSP using the distance matrix
fitness_dists = mlrose.TravellingSales(distances=distances)

# Define the optimization problem
problem = mlrose.TSPOpt(length=len(coords), fitness_fn=fitness_dists, maximize=False)

# Define the simulated annealing schedule
schedule = mlrose.ExpDecay(init_temp=10, exp_const=0.005, min_temp=1)

# Solve the problem using simulated annealing and print the result structure
result = mlrose.simulated_annealing(problem, schedule=schedule, max_attempts=100, max_iters=1000, random_state=2)
print("Result structure:", result)

# If the result is a tuple, unpack it accordingly
if isinstance(result, tuple) and len(result) == 2:
    best_state, best_fitness = result
else:
    best_state, best_fitness = result[0], result[1]

# Display the results
print("Best route found:", best_state)
print(f"Total distance of best route: {best_fitness:.3f}")