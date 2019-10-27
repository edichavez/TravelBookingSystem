# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:43:22 2019

@author: edita
"""

import turtle 

tim = turtle.Turtle()
tim.color('blue')
tim.pensize(1)
tim.shape('turtle')

x= 100

def KotchCurve(tim,x):
    for i in range(2):
        tim.pd()
        tim.forward(x/(4**i))
        tim.setheading(60)
        tim.forward(x/(4**i))
        tim.setheading(300)
        tim.forward(x/(4**i))
        tim.setheading(0)
        tim.forward(x/(4**i))

def KochSnowflake():
    pass