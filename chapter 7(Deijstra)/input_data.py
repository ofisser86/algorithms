graph = {}
cities_list = {}
numbers_of_tests = int(input('Enter number of tests -->'))
numbers_of_cities = int(input('Enter numbers of cities -->'))

i = 0
while i < numbers_of_cities:
    city_name = input('Enter city name -->')
    graph[city_name] = city_name
    graph[city_name] = {}
    number_of_neighbors = int(input('Enter number of neighbors -->'))
    for j in range(0, number_of_neighbors):
        index_connected_to_city_name, transportation_cost = input().split()
        index_connected_to_city_name = int(index_connected_to_city_name)
        transportation_cost = int(transportation_cost)
        graph[city_name][index_connected_to_city_name] = transportation_cost
    i += 1

source_city, destination_city = input('Source and destination cities -->').split()

print(graph)