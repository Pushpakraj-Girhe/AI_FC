import random

def hill_climb(func, start, step=1):
    current = start
    while True:
        print(f"Current: {current}, Value: {func(current)}")
        neighbors = [current - step, current + step]
        best_neighbor = max(neighbors, key=func)
        if func(best_neighbor) <= func(current):
            break
        current = best_neighbor
    print("Best solution:", current)

# Example function (maximize x^2)
def example_function(x):
    return -(x - 3) ** 2 + 9

hill_climb(example_function, random.randint(0, 10))
