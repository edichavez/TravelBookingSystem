# TravelBookingSystem

PROBLEM: Create a program to find the fastest route to travel from place X to place Y.

This problem can be divided in two parts: 
1) Obtaining a graph of all stops between X and Y joined by all possible paths. Our program would have to search different databases and organise nodes and edges of this graph as classes so we can easily access their information.
2) Running Dijkstra's algorithm on the graph in order to find the shortest path and printing that route.

FIRST APPROACH
I will construct a simplified graph instead of searching for real information. Here our route X-Y will be from home in Bristol to a hotel in Edinburgh, but the function can find the shortest path between any two of the stops. The different stops will be:

A = Home Bristol;
B = Coach Station Bristol;
C = Airport Bristol
D = Coach Station Edinburgh
E = Airport Edinburgh
F = Hotel Edinburgh
G = Somewhere Else (use this just to demonstrate what happens if there are no available routes)

And the paths will be by taxi, bus or walk from home to or from the airports/coach stations and coach or plane in the middle.

My places and paths are members of the Places and Paths classes respectively. This allows me to store the information I will need to perform the algorithm, such as temporary labels or lists of neighbouring places.

My algorithm is a simple while loop that stops when Y has been fixed (i.e. visited). 

TO RUN IT
Simply download the folder and run the system.py module.
