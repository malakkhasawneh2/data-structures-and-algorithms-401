# pr: https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/26

# Graphs
In this module, we are creating a Graph class represented as an adjacency list

## Challenge
Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency
An adjacency list (hash table) was the chosen data structure to use for the Graph and a list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

Adding key/value pairs and getting values from the adjacency list is essentially O(1) for time for both posting and getting. Big O is always looking for the worst case scenario. The worst case would be the length of the linked list at any given index. Say one index had 5 colisions, the Big O for time would be O(5) in that case for time.

## API
1. add_node(value): adds a new vertex to the graph, returns the added vertex<br><br>
2. add_edge(vertex1, vertex2, [weight]): adds new edge between two virtices, takes in two verticies, has ability to add weight<br><br>
3. get_nodes( ) - returns all of the vertices as a collection<br><br>
4. get_neighbors(vertex): returns a collection of vertices (with weights) connected to a vertex, takes in a vertex<br><br>
5. get_values(vertex): returns the value from a given vertex<br><br>
6. size( ) - returns number of vertices in Graph; integer<br><br>
7. breadth_first(vertex): traverses the graph starting from the given vertex, returns a list of nodes visited during traversal
