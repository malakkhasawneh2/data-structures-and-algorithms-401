from graph.graph import Graph
import inspect, re, collections


class NewGraph(Graph):
    def breadth_first(self, vertex):
        """
        Traverses the graph from starting node to neighboring nodes
        Parameters:
            [vertex] - Starting vertex for breadth_first traversal
        Return:
            [list] - List of nodes visited during traversal; in order
        """
        visited_vertices = set()
        q = collections.deque()
        q.appendleft(vertex)
       
        while q:
            current = q.pop()
            visited_vertices.add(current)
            lst = self.get_neighbors(current)
            if lst:
                for edge in lst:
                    if edge[0] not in visited_vertices:
                        q.appendleft(edge[0])
        
        return visited_vertices


class Vertex:
    """
    Instance of a vertex object
    Attributes:
        [value] - requires a value to init
    """
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

if __name__ == "__main__":
    graph = NewGraph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    # add all edges
    graph.add_edge(apple, banana, 1)

    graph.add_edge(banana, apple, 2)
    graph.add_edge(banana, cantelope, 3)
    graph.add_edge(banana, figs, 4)

    graph.add_edge(cantelope, banana, 5)
    graph.add_edge(cantelope, figs, 6)
    graph.add_edge(cantelope, dates, 7)

    graph.add_edge(figs, banana, 8)
    graph.add_edge(figs, cantelope, 9)
    graph.add_edge(figs, dates, 10)
    graph.add_edge(figs, eggplant, 20)

    graph.add_edge(dates, cantelope, 30)
    graph.add_edge(dates, figs, 40)
    graph.add_edge(dates, eggplant, 50)

    graph.add_edge(eggplant, figs, 60)
    graph.add_edge(eggplant, dates, 70)

    print(graph.breadth_first(apple))





    