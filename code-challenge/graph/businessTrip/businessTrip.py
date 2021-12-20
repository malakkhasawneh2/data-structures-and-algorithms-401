from graph.graph import Graph


def businessTrip(graph, cities):
    price = 0
    is_neighbor = False

    if not cities:
        return f'{is_neighbor} : ${price}'

    nodes = graph.get_nodes()
    if not nodes:
        return f'{is_neighbor} : ${price}'
        
    city_nodes = []
    for city in cities:
        for node in nodes:
            if city == node.value:
                city_nodes.append(node)
    if len(cities) != len(city_nodes):
        return f'{is_neighbor} : ${price}'

    neighbors = graph.get_neighbors(city_nodes[0])

    for i in range(1, len(city_nodes)):
        is_neighbor = False
        for neighbor in neighbors:
            if neighbor[0] == city_nodes[i]:
                price += neighbor[1]
                is_neighbor = True
                break
        if not is_neighbor:
            return f'{is_neighbor} : $0'
        neighbors = graph.get_neighbors(city_nodes[i])

    return f'{is_neighbor} : ${price}'
