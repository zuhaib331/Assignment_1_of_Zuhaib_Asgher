# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:00:49 2018

@author: Zuhaib Asghar
"""

import turtle

def draw_name(some_turtle):
     some_turtle.forward(100)
     a=some_turtle.position()
     print(a)
     some_turtle.left(-125)
     some_turtle.forward(135)
     some_turtle.right(-125)
     some_turtle.forward(100)

       
            
       
def draw_art():
    
   window = turtle.Screen()
   
   window.bgcolor("red")
   ben = turtle.Turtle()
   ben.shape("turtle")
   ben.color("yellow")
   ben.speed(1)
        
   draw_name(ben)
        
   window.exitonclick()
    
draw_art()
