##TEKTowr ASSESSMENT: TRAVEL BOOKING SYSTEM
#Creating a program that finds the fastest route from X to Y

#PART 1: OUR GRAPH: Vertices are places, edges are means of trasnport.
import random

class Place:
    #Create the vertices of our graph, the Places class, ready to perform 
    #the algorithm.
    
    def __init__(self,name):
        self.name = name
        self.temp_label = True
        self.label = float("inf")
        self.neighbours = []
        self.preceeding = []
        
    def assign(self,value):
        self.label = value
        
    def fix(self):
        self.temp_label = False
        
    def adjacent(self,path):
        if path.origin == self:
            self.neighbours.append(path)
        elif path.destination == self:
            self.preceeding.append(path)
            
    def what_neighbours(self):
        if self.neighbours == []:
            print ('No forward neighbours found')
        else:
            print (self.name + ' has neighbours:' )
            for i in self.neighbours:
                print (i.destination.name + ' via ' + i.id )
                
    def what_preceeding(self):
        if self.preceeding == []:
            print ('No preceeding places found')
        else:
            print (self.name + ' has preceeding neighbours:' )
            for i in self.preceeding:
                print (i.origin.name + ' via ' + i.id )

    def info(self):
        if self.temp_label == True:
            print ('%s has temporary label of %g' %(self.name, self.label))
        else:
            print ('%s has a fixed label of %g' %(self.name, self.label))
    
#Now we create a class of paths, together with some subclasses. We can ask for 
#information about them and also get how long the journey will take.
#Note that the ORIGIN and DESTINATIONS are from the Places class above
class Path:
    #Create the graph connecting all PLaces
    def __init__(self,id,origin,destination,length):
        self.id = id 
        self.origin = origin 
        self.destination = destination
        self.length = length
        self.time = self.length
        
    def info_path(self):
        print('%s goes from %s to %s, taking %g hrs.' 
              % (self.id, self.origin.name, self.destination.name, self.length))
        
    def how_long(self):
        time = self.length
        hrs,mi = divmod(time,1)
        mi = int(mi*60)
        print(' %g hrs %g mins' %(hrs,mi))
 
class Plane(Path):
    #Each different type of path will have extra bits
    #always arrive 2hrs early to the airport
    arriving_time = 2 
    #control time depends on the destination airport
    def __init__(self,id, origin,destination,length,control_time):
        super().__init__(id,origin, destination, length)
        self.control_time = control_time
        self.time = self.length + self.control_time + self.arriving_time
        
    def info_path(self):
        print('%s goes from %s to %s, taking %g hrs in total, with waiting times.' 
              % (self.id,self.origin.name, self.destination.name, self.length + 
                 self.arriving_time + self.control_time))
        
    def how_long(self):
        time = self.length + self.control_time + self.arriving_time
        hrs,mi = divmod(time,1)
        mi = int(mi*60)
        print(' %g hrs %g mins' %(hrs,mi))
    
class Car(Path):
    #Each different type of path will have extra bits
    #A car will be subject to traffic delay, which is a random percentage of
    #the path length, no more than 50% extra.
    def __init__(self,id, origin,destination,length):
        super().__init__(id,origin, destination, length)
        self.traffic_delay=random.uniform(1,1.5)
        self.time = self.length*self.traffic_delay
        
    def info_path(self):
        print('%s goes from %s to %s, taking %g hrs, with traffic.' 
              % (self.id,self.origin.name, self.destination.name, 
                 self.length*self.traffic_delay))
        
    def how_long(self):
        time = self.length*self.traffic_delay
        hrs,mi = divmod(time,1)
        mi = int(mi*60)
        print(' %g hrs %g mins' %(hrs,mi))

class Coach(Car):
    #Each different type of path will have extra bits
    #A coach is subject to traffic, just as cars, but also delays 10% of the
    #travel time due to stops along the way.
    delay = 1.1 
    def __init__(self, id, origin,destination,length):
        super().__init__(id,origin, destination, length)
        self.traffic_delay = random.uniform(1,1.5)
        self.time = self.delay*self.length*self.traffic_delay
    
    def info_path(self):
        print('%s goes from %s to %s, taking %g hrs in total, with traffic and stops'
              % (self.id, self.origin.name, self.destination.name, 
                 self.delay*self.length*self.traffic_delay))
        
    def how_long(self):
        time = self.delay*self.length*self.traffic_delay
        hrs,mi = divmod(time,1)
        mi = int(mi*60)
        print(' %g hrs %g mins' %(hrs,mi))
    

    
#OUR GRAPH SET UP 
    
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
        
        
#NOW THE ALGORITHM
              
def Take_me_somewhere():
    #This first part obtains the start and end of the journey, which must be 
    #one of our stored places.
    print('I can find the fastest route to where you want to go.')
    while True:
        try:
            X = input('First of all, where are you now? ')
        except ValueError:
            print('Sorry, I didn\'t catch that.')
            continue
        if X not in (i.name for i in places):
            print('Sorry, that place is not in my list, try again?')
            continue
        else:
            break
    X = next(i for i in places if i.name == X)
    while True:
        try:
            Y = input('Ok, and where do you want to go to? ')
        except ValueError:
            print('Sorry, I didn\'t catch that')
            continue
        if Y not in (i.name for i in places):
            print('Oops I don\'t know that place, try again?')
            continue
        else:
            break
    Y = next(i for i in places if i.name == Y)
    print ('Great, let\'s get you from %s to %s...' %(X.name, Y.name) )
    
    #We now have X and Y, let's run the algorithm.
    X.assign(0)
    while Y.temp_label == True:
        minlabel = min(i.label for i in places if i.temp_label == True)
        K = next(i for i in places if 
             (i.label == minlabel and i.temp_label == True))
        K.fix()
        for i in K.neighbours:
            i.destination.label = min(i.destination.label,
                                      K.label+i.time)
            K.fix()
    if Y.label == float('inf'):
        print ('It is impossible to get to %s from %s.' %(Y.name, X.name))
    else:
        hrs,mi = divmod(Y.label,1)
        mi = int(mi*60)
        print('We have found your path!'
              'It will take %g hrs %g minutes.' %(hrs,mi))
        #Now we will search for a route that will achieve this minimum.
        node = Y #we start to search from the end
        route =[] #we will store the route here
        #print(total)
        while node.label != 0:
            searching_path = next(i for i in node.preceeding if (node.label-i.time == i.origin.label))
            route.append([searching_path.destination.name, searching_path.id,
                          searching_path.time])
            node = searching_path.origin
    route.reverse()
    print ('\n Follow this route from %s:' % X.name)
    for i in route:
        print('go to %s via %s, takes %g hrs,' % (i[0],i[1],i[2]))
    return Y.label,route