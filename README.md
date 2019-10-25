# TravelBookingSystem

PROBLEM: Create a program to find the fastest route to travel from place X to place Y.

This problem can be divided in two parts: 
1) Obtaining a graph of all stops between X and Y joined by all possible paths. Our program would have to search different databases and organise nodes and edges of this graph as classes so we can easily access their information.
2) Running Dijkstra's algorithm on the graph in order to find the shortest path and printing that route.

FIRST APPROACH
On this first attempt, I will construct a simplified graph instead of searching for real information. Here our route X-Y will be from home in Bristol to a hotel in Edinburgh. The different stops will be:

A = Home in Bristol;
B = Coach Station in Bristol;
C = Airport in Bristol
D = Coach Station in Edinburgh
E = Airport Station in Edinburgh
F = Hotel in Edinburgh

And the paths will be by taxi, bus or walk from home to or from the airports/coach stations and coach or plane in the middle.

My places and paths are members of the Places and Paths classes respectively. This allows me to store the information I will need to perform the algorithm, such as temporary labels at the nodes and length of edges (how long paths take vary depending on what subclass they are).

My algorithm is a simple two step iteration and stops when all labels have been fixed or if all temporary labels are infinity and returns the route taken if found. The statement of the algorithm I use is as follows, from start X to finish Y.


1. Assign a temporary label l_i = infty to all vertices except for X, l_X=0.
2. Find vertex K with smallest temporary label l_K. Make it permanent and call it L_K. If K=Y, stop, path has been found.
3. For each vertex J with a temporary label, determine the smallest of l_J and l_K+d_KJ (d_KJ=shortest edge from K to J) and assing this value to l_J. If there are any temporary labels not infinity, return to step 2, otherwise go to step 4.
4. The vertices with temporary labels all have labels of infinity so the algorithm must stop, there is no path from X to Y.

In my program, step 2 above is called Step1 and step 3 above is called Step2, these are the functions iterated until algorithm stops.

Simply download the script and run it, and change the starting and ending points in Dijkstra(A,F,places,paths) to find different routes.

FURTHERMORE
This method was my first thought, as I tried to show my understanding of classes, but after researching the implementation of Dijkstra's algorithm, I found it would be best to do it using an adjacency matrix to represent the graph
