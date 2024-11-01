# Animation from PI
#
# Based on Youtube-Series from Graviatar 
# https://www.youtube.com/playlist?list=PLhC_4AWNg9rklYLWPZmOKeNEW3LcwN5lz
#
# visualisation after method from Nadieh Brehmer 
# https://www.scientificamerican.com/blog/sa-visual/the-boundless-beauty-of-pi/

import turtle as tu

lines = 100_000

with open ( "One_Mill_Pi.txt","r" ) as f:

    pi = f.read()

tu.mode("logo")
tu.tracer(False)
tu.screensize(6000,6000,"black")
#tu.pencolor("red")
tu.colormode(255)

for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255,255-color,color)
    number = int(pi[n])
    rotation = number * 36
    tu.setheading(rotation)
    tu.forward(3)
    if n % 10_000 == 0:
        tu.update()
tu.done()
