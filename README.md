# Vehicle Routing Problem

Uses Tabu search to explore list of possible optimal routes.

Run `pip install gpxpy` command to install gpxpy package that is responsible for distance calculation between nodes.

Use command ```python solver.py``` to run the algorithm.
Adjust the number of iterations using `max_iterations` variable in solver.py.
Number of vehicles set to 25, demand of each node is 1, there's no load restriction for a vehicle.

The output has the following format: vehicle number followed by the ordered list of nodes to visit.
`node 1` indicates depot and the rest of the numbers correspond to the position of entry in location file.
So route for vechile 1 is following: depot -> location 7 -> location 6 -> location 122 -> ... location 9 -> depot, which corresponds to one of the circuit on the graph of location.
Please note that since algorithm is heuristic it may not yield the same result for every run.

```
vehicle 1:
1
7
6
122
24
25
2
5
4
9
1

vehicle 2:
1
17
13
12
157
10
29
15
16
11
1

...
```
