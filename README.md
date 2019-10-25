# TravelBookingSystem

PROBLEM: Create a program to find the fastest route to travel from place X to place Y.

This problem can be divided in two parts: 
1) Obtaining a graph of all stops between X and Y joined by all possible paths. Our program would have to search different databases and organise nodes and edges of this graph as classes so we can easily access their information.
2) Running Dijkastra's algorithm on the graph in order to find the shortest path and printing that route.

FIRST APPROACH
On this first attempt, I will construct a simplified graph instead of searching for real information. Here our route X-Y will be from home in Bristol to a hotel in Edinburgh. The different stops will be:
A = Home in Bristol
B = Coach Station in Bristol
C = Airport in Bristol
D = Coach Station in Edinburgh
E = Airport Station in Edinburgh
F = Hotel in Edinburgh
And the paths will be by taxi, bus or walk from home to or from the airports/coach stations and coach or plane in the middle.

My places and paths are members of the Places and Paths classes respectively. This allows me to store the information I will need to perfomr the algorithm, such as temporary labels at the nodes and length of edges.

My algorithm is a simple two step iteration and stops when all labels have been fixed.

