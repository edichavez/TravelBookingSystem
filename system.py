''' Run this to get from Bristol to Edinburgh '''
#OUR GRAPH SET UP 
from set_up import Take_me_somewhere,Place,Path,Coach,Car,Plane
#Places for us to use
A = Place ('Home Bristol')
B = Place ('Coach Station Bristol')
C = Place ('Airport Bristol')
D = Place ('Coach Station Edinburgh')
E = Place ('Airport Edinburgh')
F = Place ('Hotel Edinburgh')
G = Place ('Somewhere Else')

#These are our different paths.
#travelling to the Coach station by taxi, bur or walk, etc.
taxi2coach = Car('Taxi1',A,B,0.5)
taxi2air = Car('Taxi2',A,C,1)
bus2coach = Coach ('Bus1',A,B,0.7)
bus2air = Coach ('Bus2',A,C, 1.5)
walk2coach = Path('Walk1',A,B,1.1)
walk2air = Path ('Walk2',A,C,2.1)

megabus = Coach ('Coach',B,D,6)
plane = Plane('Plane',C,E,1.5,1) #plane needs control time

coach2taxi = Car('Taxi3',D,F,0.3)
air2taxi = Car('Taxi4',E,F,0.6)
coach2bus = Coach ('Bus3',D,F,0.5)
air2bus = Coach ('Bus4',E,F, 0.8)
coach2walk = Path ('Walk3',D,F,0.8)
air2walk = Path ('Walk4',E,F,1.6)

#We put these in two lists to refer to during the algorithm
places = [A,B,C,D,E,F,G]
paths = [taxi2coach,taxi2air,bus2coach,bus2air, walk2coach,walk2air,
         megabus,plane,
         coach2taxi,air2taxi,coach2bus,air2bus,coach2walk,air2walk]
#This bit adds preceeding and neighbours to each place in our list
for i in places:
    for j in paths:
        i.adjacent(j)

Take_me_somewhere(places,paths)
        
