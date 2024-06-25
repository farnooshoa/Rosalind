'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Rabbits and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 004
URL: http://rosalind.info/problems/fib/
'''

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        fib_sequence = [1, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + k * fib_sequence[-2])

        return fib_sequence[-1]

# Example usage:
n_value = 4

k_value = 2
result = rabbit_pairs(n_value, k_value)
print(result)
