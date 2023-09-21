Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
... import colorsys
... import math
... 
... speed(0.25)
... bgcolor("black")
... 
... # Genera los petalos
... goto(0, -40)
... h = 0
... 
... for i in range(16):
...     for j in range(18):
...         c = colorsys.hsv_to_rgb(0.125, 1, 1)
...         color(c)
...         rt(90)
...         circle(150 - j * 6, 90)
...         lt(90)
...         circle(150 - j * 6, 90)
...         rt(180)
...     circle(40, 24)
... 
... # Genera la parte central de la flor
... color("black")
... shape("turtle")
... fillcolor("brown")
... phi = 137.508 * (math.pi / 180.0)
... 
... for i in range(200):
...     r = 4 * math.sqrt(i)
...     theta = i * phi
...     x = r * math.cos(theta)
...     y = r * math.sin(theta)
...     penup()
...     goto(x, y)
...     setheading(i * 137.508)
...     pendown()
...     stamp()
... 
... # Agrega el mensaje
... penup()
... goto(0, 300)
... color("red")
... write("Gracias por ser parte de mi vida, te amo mi angiesitaa hermosa", align="center", font=("Arial", 12, "bold"))
... hideturtle()
... done()
... 
... 
