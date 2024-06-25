import numpy as np

def rabbit_pairs_dynamic(n, m):
    population = np.zeros([n+1,m], dtype=np.int64)
    population[1][0] = 1

    for month in range(2,population.shape[0]):
        for age in range(0,population.shape[1]):
            if age == 0:
                population[month][age] = np.sum(population[month-1,1:])
            else:
                population[month][age] = population[month-1][age-1]

    return np.sum(population[n])


# Example usage
n = 86
m = 18
result = rabbit_pairs_dynamic(n, m)
print(result)
