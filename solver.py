import random
import sys
import time

import pacman


class Inidividual(object):
	def __init__(self):
		self.numchros = 200
		self.dirs = ["l", "r", "u", "d"]
		self.moves = [self.dirs[random.randint(0, 3)] for i in range(self.numchros)]
		self.fitness = float("inf")

	def mutate(self):
		self.moves[random.randint(0, self.numchros-1)] = self.dirs[random.randint(0, 3)]

	def scramble(self):
		for i in range(self.numchros):
			self.mutate()

	def payoff(self):
		self.fitness = pacman.main(self.moves)[0]


def main(argv):
	maxfit = pacman.main("l")[1]
	popsize = 1000
	time_start = time.clock()
	population = [Inidividual() for i in range(popsize)]
	generation = 0
	while(True):
		for individual in population:
			individual.payoff()
		population.sort(key = lambda x: x.fitness, reverse = True)
		print("Generation {0:04d}, best solution: {1:03d}/{2:03d} points. Time taken: {3:09.4f} seconds."\
			.format(generation, population[0].fitness, maxfit, time.clock()-time_start))
		if (population[0].fitness >= maxfit):
			print("Moves:\n{0}".format(population[0].moves))
			return population[0].moves
		for individual in population[popsize//4:popsize//2]:
			individual.mutate()
		for individual in population[popsize//2:]:
			individual.scramble()
		generation += 1


if __name__ == "__main__":
	main(sys.argv)