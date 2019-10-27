import turtle

angles_curve = [60,-120,60,0]
def KochCurve(tim,x,index):
    if index>0:
        for i in angles_curve:
            KochCurve(tim,x,index-1)
            tim.setheading((tim.heading()+i)%360)
    else:
        tim.forward(x)
        
def KochSnowflake(x,tim,index):
    for i in range(3):
        KochCurve(tim,x,index)
        tim.right(120)   
        
def fractals():
    tim = turtle.Turtle()
    tim.pensize(1)
    tim.shape('turtle')
    tim.pu()
    tim.goto(-150,150)
    tim.pd()

    colours = ['sandy brown', 'orange red','saddle brown','olive','teal','steel blue']
    for i in colours:
        tim.color(i)
        KochSnowflake(1000/(3**(colours.index(i)+1)),tim,colours.index(i))

print('As well as beautiful to look at and probably great for mindfulness,'
      +'fractals are being studied by people in biomimicry. If nature uses these structures,'
      + 'we should too! Iterative methods are used in image compression, computer graphics..'
      +'and I think these heat exchangers and test tubes are really cool!'
      +'http://fractalfoundation.org/OFC/OFC-12-2.html. ')

fractals()
