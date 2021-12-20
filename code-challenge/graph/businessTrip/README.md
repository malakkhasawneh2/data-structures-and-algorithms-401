# Challenge Summary
In this module, we are creating a function that checks if there is an businessTrip or series of consecutive businessTrips that exists between a list of nodes (represented by their values).

If there is no such 'businessTrip', we will return 'False : $0'.

If there is such an 'businessTrip', we will return 'True : $[cost]'

## Whiteboard Process
![Whiteboard Solution]()
![Whiteboard Solution]()

## Approach & Efficiency
Function, businessTrip, takes a graph and list of values as arguements. Determines if there are nodes in the graph with those values from the list. Determines if there are edges between adjacent nodes from the value_list. Returns True or False if there are edges between every node in the list - start to finish AND the cost of traversing those edges.

This solution seems to be close to O(N^2) for time. We need to go through each unique node once, then for each node we need to check all of its neighbors. If this was a complete graph (all vertices pointing to all others) this would 100% be an O(N^2) for time. Maybe it is best to say that in that 'worst case' this method is O(N^2) for time efficency.

For space efficency it is O(N). We are creating a list of nodes that is exactly N nodes in length.
## Solution

businessTrip(graph, value_list):

Parameters:
- [graph] - the graph to be checked for an "businessTrip" and cost
- [value_list] - list of values representing nodes in the graph. Ordered from start to finish.

Return: 
- [string] - formatted string of "boolean : $cost"
