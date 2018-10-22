from graph import Graph
from road import Road
from city import City

def read_file(filename):
    file = open(filename, 'r')
    return [line.split() for line in file]

def add_cities(filename, graph):
    for city in read_file(filename):
        graph.add_city(City(city[0], (city[1], city[2])))

def add_roads(filename, graph):
    for road in read_file(filename):
        try:
            from_city = graph.search_city(road[0])
            to_city = graph.search_city(road[1])
            length = road[2]

            graph.add_road(Road(from_city, to_city, length))
        except:
           print('city not found')


if __name__ == '__main__':
    graph = Graph()
    add_cities('positions.txt', graph)
    add_roads('connections.txt', graph)
    print(graph)
