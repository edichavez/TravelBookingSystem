# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:28:53 2019

@author: edita
"""

##TEKTowr ASSESSMENT: TRAVEL BOOKING SYSTEM
#Creating a program that finds the fastest route from A to B

#PART 1: OUR GRAPH: Vertices are places, edges are means of trasnport.
import random
class Place:
    #Create the vertices of our graph, the Places class, ready to perform 
    #the algorithm.
    def __init__(self,name,visited = False, temp_label = True,label = float("inf")):
        self.name = name
        self.visited = visited
        self.temp_label = temp_label
        self.label = label
        
    def visit(self):
        self.visited = True
        
    def assign(self,value):
        self.label = value
        
    def fix(self):
        self.temp_label = False
        
    def info(self):
        if self.visited == False:
            print('%s has not yet been visited, thus label is infinity'
                  %self.name)
        elif self.visited == True and self.temp_label == True:
            print ('%s has temporary label of %g' %(self.name, self.label))
        else:
            print ('%s has a fixed label of %g' %(self.name, self.label))

#Now we create a class of paths, together with some subclasses. We can ask for 
#information about them and also get how long the journey will take.
#Note that the ORIGIN and DESTINATIONS are from the Places Class above
class Path:
    #Create the graph connecting all PLaces
    def __init__(self,origin,destination,length):
        self.origin = origin 
        self.destination = destination
        self.length= length
        
    def info_path(self):
        print('From %s to %s, taking %g hrs.' 
              % (self.origin.name, self.destination.name, self.length))
        
    def how_long(self):
        return self.length
 
class Plane(Path):
    #Each different type of path will have extra bits
    #always arrive 2hrs early to the airport
    arriving_time = 2 
    #control time depends on the destination airport
    def __init__(self, origin,destination,length,control_time):
        super().__init__(origin, destination, length)
        self.control_time = control_time
        
    def info_path(self):
        print('From %s to %s, taking %g hrs in total (with waiting times).' 
              % (self.origin.name, self.destination.name, self.length + 
                 self.arriving_time + self.control_time))
        
    def how_long(self):
        return self.length + self.control_time + self.arriving_time
    
class Car(Path):
    #Each different type of path will have extra bits
    #raffic delay is random but under 1hr.
    def __init__(self, origin,destination,length,
                 traffic_delay=random.uniform(0,1)):
        super().__init__(origin, destination, length)
        self.traffic_delay = traffic_delay
        
    def info_path(self):
        print('From %s to %s, taking %g hrs but traffic makes you %g hrs late.' 
              % (self.origin.name, self.destination.name, 
                 self.length, self.traffic_delay))
        
    def how_long(self):
        return self.length + self.traffic_delay

class Coach(Car):
    #Each different type of path will have extra bits
    #A coach is subject to traffic, just as cars, but also delays 10% of the
    #travel time due to stops along the way.
    def __init__(self, origin,destination,length,
                 traffic_delay=random.uniform(0,1), stops_delay = None):
        super().__init__(origin, destination, length, 
             traffic_delay)
    
    def info_path(self):
        print('From %s to %s, taking %g hrs but traffic and stops' +
              'make you %g hrs late.' 
              % (self.origin.name, self.destination.name, 1.1*self.length, 
                 self.traffic_delay))
        
    def how_long(self):
        return 1.1*self.length + self.traffic_delay
    

    
#Places for us to use
#Places for us to use
A = Place ('Home Bristol')
B = Place ('Coach Station Bristol')
C = Place ('Airport Bristol')
D = Place ('Coach Station Edinburg')
E = Place ('Airport Edinburg')
F = Place ('Hotel Edinburg')

taxi2coach = Car(A,B,0.5)
taxi2air = Car(A,C,1)
bus2coach = Coach (A,B,0.7)
bus2air = Coach (A,C, 1.5)
walk2coach = Path(A,B,1.1)
walk2air = Path (A,C,2.1)

megabus = Coach (B,D,6)
plane = Plane(C,E,1.5,1) #plane needs control time

coach2taxi = Car(D,F,0.3)
air2taxi = Car(E,F,0.6)
coach2bus = Coach (D,F,0.5)
air2bus = Coach (E,F, 0.8)
coach2walk = Path (D,F,0.8)
air2walk = Path (E,F,1.6)

places = [A,B,C,D,E,F]
paths = [taxi2coach,taxi2air,bus2coach,bus2air, walk2coach,walk2air,
         megabus,plane,
         coach2taxi,air2taxi,coach2bus,air2bus,coach2walk,air2walk]

#ALGORTIHM FUNCTION
  
#Create the algorithm, using Dijkastra's method for shortest path finding.
#I have created the two steps that Dijkastra's fuction will call.

def step1(places, B):
    nodes = [x for x in places if x.visited == True and x.temp_label == True]
    #This step fixes the minimum temporary label and stops 
    #the algorithm when arriving at the end point.
    for x in places:
        while x in nodes:
            if x.label == min(i.label for i in nodes):
                x.temp_label = False
                k = x.name
                print ()
                if k == B.name:
                    print('You have found your route to %s!' %B.name)
                    break
                step2(places,paths,k,A,B)

def step2(places,paths,k,A,B):
    nodes = [[x] for x in places if x.temp_label == True]
    print([i[0].name for i in nodes])
    for i in nodes:
        i.append(x for x in paths 
             if x.origin == k and x.destination == i[0].name)
    
        for j in i[1:]:
            print(j)
            i[0].label = min(i[0].label,i[0].label+j.how_long())
    for i in places:
        if i.label == float('inf'):
            step1(places,B)
        else:
            print ('There is no path from %s to %s' % (A.name, B.name))
            break
        
def Dijkastra(A,B,places,paths):
    A.assign(0)
    A.visit()
    step1(places,B)
    print ('The route is as follows' (i.name, i.label for i in places))
    
    

    