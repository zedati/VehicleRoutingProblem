import sys
import math
import gpxpy.gpx
import csv
import primitives

FLEET_SIZE = 25
CAPACITY = 2**32     # no capacity limitations
DEPOT_LOCATION = (11.552931,104.933636)

def _read_locations():
    reader = csv.reader(open("locations.csv", "rt"), delimiter=",")
    locations = list(reader)
    try:
        res = [(float(l[0]), float(l[1])) for l in locations]
    except IndexError as e:
        print(e)
        raise e
    return res

class DataMapper(object):

    def __init__(self):
        self.locations = _read_locations()
        self.locations.insert(0, DEPOT_LOCATION)    # adding depot to the locations
        self.network = self._create_network(self.locations)
        self.fleet = self._create_fleet(CAPACITY, FLEET_SIZE)
        self.distance_matrix = self._compute_distance_matrix(self.locations)

    def _create_network(self, node_coordinates_list):
        network = primitives.Network()
        demand_array = [1] * len(node_coordinates_list) # demand of all nodes is 1
        demand_array[0] = 0     # no demand for depot

        for id_, (node_coords, demand) in enumerate(zip(node_coordinates_list, demand_array)):
            node = primitives.Node(id_ + 1, node_coords, demand)
            network.append_node(node)
        network[0].visited = True
        return network

    def _create_fleet(self, capacity, number_of_vehicles=0):
        vehicles_left = int(number_of_vehicles)
        capacity = int(capacity)
        fleet = []
        while (vehicles_left):
            vehicle = primitives.Vehicle(capacity)
            fleet.append(vehicle)
            vehicles_left -= 1
        return fleet

    def _compute_distance_matrix(self, locations):
        nb_nodes = len(locations)
        distance_matrix = [[None for i in range(nb_nodes)] for j in range(nb_nodes)]
        for i in range(nb_nodes):
            distance_matrix[i][i] = 0
            for j in range(nb_nodes):
                dist = gpxpy.geo.haversine_distance(locations[i][0], locations[i][1], locations[j][0], locations[j][1])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist
        return distance_matrix
