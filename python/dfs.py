cities_map = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# Option 1:
# def dfs(cities_map, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(cities_map[vertex] - visited)
#     return visited
#
# visited = dfs(cities_map, 'Boston')
# print(visited)


# # Option 1: with pathing
# def dfs_paths(cities_map, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         for city in cities_map[vertex] - set(path):
#             if city == goal:
#                 yield path + [city]
#             else:
#                 stack.append((city, path + [city]))
#
# print(list(dfs_paths(cities_map, 'Portland', 'New York')))
#


# Option 2:
# def dfs(cities_map, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for city in cities_map[start] - visited:
#         dfs(cities_map, city, visited)
#     return visited
#
# visited = dfs(cities_map, 'Portland')


# Option 2: with pathing
def dfs_paths(cities_map, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path

    print(start)
    print(cities_map[start])
    print(path)

    for city in cities_map[start] - set(path):
        yield from dfs_paths(cities_map, city, goal, path + [city])
