import turtle

def draw_square(some_turtle):
     for i in range(1,5):
          some_turtle.forward(100)
          some_turtle.right(90)
def draw_art():
     window = turtle.Screen()
     window.bgcolor("green")
     
     brad = turtle.Turtle()
     brad.shape("turtle")
     brad.color("yellow")
     brad.speed(5)
     for i in range(1,37): 
       draw_square(brad)
       brad.right(10)
     

     #gautham = turtle.Turtle()
     #gautham.shape("arrow")
     #gautham.color("blue")
     #gautham.circle(100)
     

     window.exitonclick()

draw_art()
