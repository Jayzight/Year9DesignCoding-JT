'''
Created on 6 Apr 2016

@author: aml
'''

import turtle

class TurtleHangman:
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        # Initialise turtle window and it's properties
        # self.window = turtle.Screen()
        # self.window.bgcolor("systemWindowBody")
        # self.window.setup(width = 300, height = 450, startx = None, starty = None)

        # Initialise drawing turtle
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.shape("turtle")
        self.turtle.color("black")
        self.turtle.speed(4)
        
    def draw_hang(self):
       
        self.turtle.left(90)
        self.turtle.forward(200)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.color('systemWindowBody')
        self.turtle.forward(60)
        self.turtle.color('black')
        self.turtle.left(90)
        
    def draw_head(self):
        self.turtle.circle(30)
        
    def draw_body(self):
        self.turtle.right(90)
        self.turtle.forward(70)
        
    def draw_r_hand(self):
        self.turtle.left(180)
        self.turtle.forward(70)
        self.turtle.left(135)
        self.turtle.forward(40)
        
    def draw_l_hand(self):
        self.turtle.left(180)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(40)
        
    def draw_l_leg(self):
        self.turtle.left(180)
        self.turtle.forward(40)
        self.turtle.left(135)
        self.turtle.forward(70)
        self.turtle.left(45)
        self.turtle.forward(50)
        
        
    def draw_r_leg(self):
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        
    def draw_eyes(self):
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.left(45)
        self.turtle.forward(70)
        self.turtle.color('systemWindowBody')
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.left(180)
        self.turtle.color('black')
        self.turtle.forward(15)
        self.turtle.color('systemWindowBody')
        self.turtle.forward(10)
        self.turtle.color('black')
        self.turtle.forward(15)
        self.turtle.ht()
        
    def draw_nose(self):
        self.turtle.st()
        self.turtle.left(90)
        self.turtle.color('systemWindowBody')
        self.turtle.forward(5)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.color('black')
        self.turtle.forward(15)
        self.turtle.ht()
    
    def draw_mouth(self):
        self.turtle.st()
        self.turtle.color('systemWindowBody')
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(10)
        self.turtle.color('black')
        self.turtle.left(90)
        self.turtle.circle(10, 180)
        self.turtle.ht()
        
    def update_hangman_viz(self, count):
        
        if count == 1:
            self.draw_hang()
        elif count == 2:
            self.draw_head()
        elif count == 3:
            self.draw_body()
        elif count == 4:
            self.draw_r_hand()
        elif count == 5:
            self.draw_l_hand()
        elif count == 6:
            self.draw_l_leg()
        elif count == 7:
            self.draw_r_leg()
        elif count == 8:
            self.draw_eyes()
        elif count == 9:
            self.draw_nose()
        elif count == 10:
            self.draw_mouth()
        else:
            pass
    
        
