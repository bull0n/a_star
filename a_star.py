import math

from graph import Graph
from city import City

def square(x):
    return x*x

def read_file(filename):
    '''
    return an array of line of our file
    '''
    file = open(filename, 'r')
    return [line.split() for line in file]

def add_cities(filename, graph):
    '''
    add all the city of our file into our graph
    '''
    for city in read_file(filename):
        graph.add_city(City(city[0], (city[1], city[2])))

def add_roads(filename, graph):
    '''
    add all the roads between 2 cities from a file into a graph
    '''
    for road in read_file(filename):
        # try:
            from_city = graph.search_city(road[0])
            to_city = graph.search_city(road[1])
            length = road[2]

            graph.add_road(from_city, to_city, length)
        # except:
            # print('city not found')

def heuristic_0(city1, city2):
    return 0

def heuristic_difference_x(city1, city2):
    return abs(city1.x()-city2.x())

def heuristic_difference_y(city1, city2):
    return abs(city1.y()-city2.y())

def heuristic_manhattan(city1, city2):
    return heuristic_difference_x(city1, city2)+heuristic_difference_y(city1, city2)

def heuristic_as_crows_flies(city1, city2):
    ''' distance between two city (à vol d'oiseau)'''
    x1, y1 = city1.x(), city1.y()
    x2, y2 = city2.x(), city2.y()

    return math.sqrt(square(x1-x2) + square(y1-y2))

def find_shortest_path(g, city_name1, city_name2):
    '''
    find the shortest path between 2 city
    '''
    from_city = graph.search_city(city_name1)
    to_city = graph.search_city(city_name2)

    print('\nshortest path : ')
    print('\nwith heuristic 0 : ')
    path1 = g.a_star(from_city, to_city, heuristic_0, debug = False)
    print_path(path1)
    print('\nwith heuristic x : ')
    path2 = g.a_star(from_city, to_city, heuristic_difference_x, debug = False)
    print_path(path2)
    print('\nwith heuristic y : ')
    path3 = g.a_star(from_city, to_city, heuristic_difference_y, debug = False)
    print_path(path3)
    print('\nwith heuristic manhattan : ')
    path4 = g.a_star(from_city, to_city, heuristic_manhattan, debug = False)
    print_path(path4)
    print('\nwith heuristic as crows flies : ')
    path5 = g.a_star(from_city, to_city, heuristic_as_crows_flies, debug = False)
    print_path(path5)

    return path5

def print_path(path):
    length = 0

    i = 0
    while i < len(path) - 1:
        length += path[i].connected_cities[path[i+1]]
        i += 1

    print(f'{[city.name for city in path]} length : {length}')


if __name__ == '__main__':
    graph = Graph()
    add_cities('data/positions.txt', graph)
    add_roads('data/connections.txt', graph)
    print(graph)

    path = find_shortest_path(graph, "Lisbon", "Warsaw")
