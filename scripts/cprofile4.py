# Using cProfile.Profile example
import random
import numpy as np

np.random.seed(1)

def print_msg():
    for i in range(10):
        print("Program completed")

def generate():
    data = np.random.randint(low=0, high=1_000_000, size=1_000)
    return data

def search_function(data):
    keys_to_find = np.random.randint(low=0, high=1_000_000, size=5)
    for key in keys_to_find:
        for num in data:
            if key == num:
                print("Found Key!")
                break

def main():
    data=generate()
    search_function(data)
    print_msg()

if __name__ == '__main__':
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('tottime')
    stats.print_stats()   