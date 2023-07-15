import random

# Genetic Algorithm Parameters
POPULATION_SIZE = 10
GENOME_LENGTH = 5
TARGET_GENOME = [1, 0, 1, 1, 0]
MUTATION_RATE = 0.1
MAX_GENERATIONS = 100

# Generate initial population
population = []
for _ in range(POPULATION_SIZE):
    genome = [random.randint(0, 1) for _ in range(GENOME_LENGTH)]
    population.append(genome)

# Genetic Algorithm
for generation in range(MAX_GENERATIONS):

    # Evaluate fitness of each genome
    fitness_scores = []
    for genome in population:
        fitness = sum(gene == target_gene for gene, target_gene in zip(genome, TARGET_GENOME))
        fitness_scores.append(fitness)

    # Check if the target genome has been found
    if TARGET_GENOME in population:
        print("Target genome found!")
        break

    # Selection: Tournament Selection
    selected_genomes = []
    for _ in range(POPULATION_SIZE):
        tournament = random.sample(list(enumerate(fitness_scores)), 2)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected_genomes.append(population[winner])

    # Crossover: Single Point Crossover
    offspring = []
    for i in range(0, POPULATION_SIZE, 2):
        parent1 = selected_genomes[i]
        parent2 = selected_genomes[i+1]
        crossover_point = random.randint(1, GENOME_LENGTH - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.extend([child1, child2])

    # Mutation: Bit Flip Mutation
    for i in range(POPULATION_SIZE):
        for j in range(GENOME_LENGTH):
            if random.random() < MUTATION_RATE:
                offspring[i][j] = 1 - offspring[i][j]

    # Update population with offspring
    population = offspring

    # Print the best genome and its fitness of the current generation
    best_genome = population[max(range(POPULATION_SIZE), key=lambda x: fitness_scores[x])]
    best_fitness = fitness_scores[max(range(POPULATION_SIZE), key=lambda x: fitness_scores[x])]
    print(f"Generation {generation + 1}: Best Genome = {best_genome}, Fitness = {best_fitness}")

# If the target genome was not found
if TARGET_GENOME not in population:
    print("Target genome not found.")
