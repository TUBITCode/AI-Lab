import random

# Genetic Algorithm Parameters
N = 10
L = 5
T = [1, 0, 1, 1, 0]
M = 0.1
G = 100

# Generate initial population
P = [[random.randint(0, 1) for _ in range(L)] for _ in range(N)]

# Genetic Algorithm
for I in range(G):

    # Evaluate fitness of each genome
    F = [sum(G == T for G, T in zip(G, T)) for G in P]

    # Check if the target genome has been found
    if T in P:
        print("Target genome found!")
        break

    # Selection: Tournament Selection
    S = [max(random.sample(list(enumerate(F)), 2), key=lambda x: x[1])[0] for _ in range(N)]

    # Crossover: Single Point Crossover
    O = []
    for i in range(0, N, 2):
        P1, P2 = P[S[i]], P[S[i + 1]]
        C = random.randint(1, L - 1)
        O.extend([P1[:C] + P2[C:], P2[:C] + P1[C:]])

    # Mutation: Bit Flip Mutation
    for i in range(N):
        O[i] = [1 - G if random.random() < M else G for G in O[i]]

    # Update population with offspring
    P = O

    # Print the best genome and its fitness of the current generation
    B, BF = max(enumerate(F), key=lambda x: x[1])
    print(f"Gen {I + 1}: Best Genome = {P[B]}, Fitness = {BF}")

# If the target genome was not found
if T not in P:
    print("Target genome not found.")
