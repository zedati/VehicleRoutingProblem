import tabu
import algorithm as alg
import datamapping
import greedySearch
import sys
import time

solution = alg.Solution(datamapping.DataMapper())

greedy_heuristic = greedySearch.GreedySearch(solution.solution)
greedy_heuristic.run(sort=True)
solution.value = solution.eval()
print (solution.value)


max_iterations = 10
tabu_search = tabu.TabuSearch(solution, max_iterations)
print ("Starting tabu search")

tabu_search.run()

print ("routes:")
for i, vehicle in enumerate(tabu_search.instance.solution.fleet):
    print ("\nvehicle "+ str(i+1)+": ")
    for node in vehicle.route:
        print (node.id)