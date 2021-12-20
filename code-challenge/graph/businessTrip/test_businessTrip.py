import pytest
from graph.graph import Graph
from businessTrip import businessTrip

@pytest.fixture
def made_graph():
    graph = Graph()

    # add all nodes
    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    cantelope = graph.add_node('cantelope')
    dates = graph.add_node('dates')
    eggplant = graph.add_node('eggplant')
    figs = graph.add_node('figs')

    graph.business_Trip(apple, banana, 1)

    graph.business_Trip(banana, apple, 2)
    graph.business_Trip(banana, cantelope, 3)
    graph.business_Trip(banana, figs, 4)

    graph.business_Trip(cantelope, banana, 5)
    graph.business_Trip(cantelope, figs, 6)
    graph.business_Trip(cantelope, dates, 7)

    graph.business_Trip(figs, banana, 8)
    graph.business_Trip(figs, cantelope, 9)
    graph.business_Trip(figs, dates, 10)
    graph.business_Trip(figs, eggplant, 20)

    graph.business_Trip(dates, cantelope, 30)
    graph.business_Trip(dates, figs, 40)
    graph.business_Trip(dates, eggplant, 50)

    graph.business_Trip(eggplant, figs, 60)
    graph.business_Trip(eggplant, dates, 70)

    return graph

def test_graph_empty():
    graph = Graph()
    lst = ['a','b','c']

    assert businessTrip(graph, lst) == 'False : $0'

def test_cities_empty(made_graph):
    graph = made_graph
    lst = []
    assert businessTrip(graph, lst) == 'False : $0'

def test_city_not_in_graph(made_graph):
    graph = made_graph
    lst = ['apple', 'banana', 'watermellon']
    assert businessTrip(graph, lst) == 'False : $0'

def test_graph_no_businessTrip():
    graph = Graph()
    lst = ['apple', 'banana', 'cantelope']
    # add all nodes
    graph.add_node('apple')
    graph.add_node('banana')
    graph.add_node('cantelope')
    graph.add_node('dates')
    graph.add_node('eggplant')
    graph.add_node('figs')

    assert businessTrip(graph, lst) == 'False : $0'

def test_graph_with_correct_businessTrip(made_graph):
    lst = ['apple','banana','cantelope','dates','eggplant','figs']

    assert businessTrip(made_graph,lst) == 'True : $121'

def test_one_city(made_graph):
    lst = ['apple']

    assert businessTrip(made_graph,lst) == 'False : $0'   