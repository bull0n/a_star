class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.connected_roads = []

    def __str__(self):
        return '%s [%s:%s] connected\n%s' % (
            self.name,
            self.coordinates[0],
            self.coordinates[1],
            '\n'.join([str(road) for road in self.connected_roads])
        )

    def __hash__(self):
        return str(self).__hash__()

    def __eq__(self, compared):
        if isinstance(compared, str):
            return self.name == compared
        elif isinstance(compared, City) :
            return self.name == compared.name and self.coordinates == compared.coordinates


    def connect_road(self, road):
        self.connected_roads.append(road)

    def x(self):
        return float(self.coordinates[0])

    def y(self):
        return float(self.coordinates[1])
