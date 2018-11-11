colors=['red', 'blue', 'yellow', 'green', 'orange',
         'white', 'gray']
import math
import turtle
backg=turtle.Screen()
backg.bgcolor('black')
turtle.setworldcoordinates(-600,-530,600,530)
ri=turtle.Turtle()#taiyang
sx=turtle.Turtle()#shuixing
jx=turtle.Turtle()#jinxing
dq=turtle.Turtle()#diqiu
hx=turtle.Turtle()#huoxing
mx=turtle.Turtle()#muxing
tx=turtle.Turtle()#tuxing
wugui=[ri,sx,jx,dq,hx,mx,tx]
rs=[0,21,41,51,87,294,528]
es=[0,0.206,0.0019,0.0019,0.093,0.05,0.0047]
bs=[]
def shangse(a,b):
    a.color(colors[b])
for i in range(7):
    shangse(wugui[i],i)
    wugui[i].shape('circle')
    wugui[i].speed(0)
    wugui[i].shapesize(0.4)
    B=math.sqrt(rs[i]**2-(rs[i]*es[i])**2)
    bs.append(B)
def huaguidao():
    for q in range(36000):
        for i in range(1,7):
            wugui[i].penup()
            wugui[i].goto(rs[i]*math.cos(16*q*math.pi/180*(21/rs[i])**0.6667),bs[i]*math.sin(16*q*math.pi/180*(21/rs[i])**0.6667))
            wugui[i].pendown()
            wugui[i].goto(rs[i]*math.cos(16*(1+q)*math.pi/180*(21/rs[i])**0.6667),bs[i]*math.sin(16*(1+q)*math.pi/180*(21/rs[i])**0.6667))
huaguidao()
