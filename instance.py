class ProblemInstance(object):

    def __init__(self, data_mapper):
        self.network = data_mapper.network
        self.fleet = data_mapper.fleet
        self.distance_matrix = data_mapper.distance_matrix
        self.drawer = None
        self.log_mode = 1