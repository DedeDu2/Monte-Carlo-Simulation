import numpy as np

def monte_carlo_pi(num_points):
    points_inside_circle = 0
    for _ in range(num_points):
        x, y = np.random.uniform(-1, 1, size=2)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
    return 4 * points_inside_circle / num_points

num_points = 10000
approx_pi = monte_carlo_pi(num_points)
print(f"Approximation of Pi using Monte Carlo Simulation: {approx_pi}")
