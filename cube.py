import numpy as np
import turtle as t
from time import sleep
from math import sin, cos, tan

rot = np.array([
    [ 1, 0, 0, ],
    [ 0, 1, 0, ],
    [ 0, 0, 1, ],
])

fov = 60
screen = 100
camz = 10
def line(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    t.goto(x1/((camz-z1)*tan(fov))*screen, y1/((camz-z1)*tan(fov))*screen)
    t.down()
    t.goto(x2/((camz-z2)*tan(fov))*screen,y2/((camz-z2)*tan(fov))*screen)
    t.up()

def cube(r):
    p1 = rot.dot([ -r, r, -r])
    p2 = rot.dot([ r, r, -r])
    p3 = rot.dot([ r, -r, -r])
    p4 = rot.dot([ -r, -r, -r])
    p5 = rot.dot([ -r, r, r])
    p6 = rot.dot([ r, r, r])
    p7 = rot.dot([ r, -r, r])
    p8 = rot.dot([ -r, -r, r])
    line(p1, p2); line (p2, p3); line(p3, p4); line(p4, p1)
    line(p5, p6); line (p6, p7); line(p7, p8); line(p8, p5)
    line(p1, p5); line (p2, p6); line(p3, p7); line(p4, p8)

def spin(axis):
    

t.speed(0)
t.up()

while True:
    cube(3)
    
