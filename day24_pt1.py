from aoc_utility import *

import numpy
import math

debug = False

input = ingestTextFile(("input/day24_input.txt", "input/day24_test_input.txt") [debug])
output = 0

min = (200000000000000, 7) [debug]
max = (400000000000000, 27) [debug]

def inside(x_pos, y_pos):
    return ((x_pos >= min) and (x_pos <= max) and (y_pos >= min) and (y_pos <= max))

def getIntersect(a_slope, b_slope, a_y0, b_y0):
    interceptFound = True
    x = 0; y = 0
    a = numpy.array([[-a_slope, 1], [-b_slope, 1]])
    try:
        a_inv = numpy.linalg.inv(a)
        c = numpy.array([[a_y0],[b_y0]])
        b = numpy.matmul(a_inv, c)
        x = b[0][0]
        y = b[1][0]
    except:
        interceptFound = False

    return x, y, interceptFound

def isInFuture(x_vel, x_pos, x, y_vel, y_pos, y):
    xInFuture = True; yInFuture = True
    if x_vel > 0 and x > x_pos:
        xInFuture = True
    elif x_vel < 0 and x < x_pos:
        xInFuture = True
    else:
        xInFuture = False

    if y_vel > 0 and y > y_pos:
        yInFuture = True
    elif y_vel < 0 and y < y_pos:
        yInFuture = True
    else:
        yInFuture = False
    
    return (xInFuture and yInFuture)

class Hailstone:
    def __init__(self, data):
        self.x_pos = int(data.split(',')[0])
        self.y_pos = int(data.split(',')[1])
        self.z_pos = int(data.split(',')[2].split('@')[0])
        self.x_vel = int(data.split(',')[2].split('@')[1])
        self.y_vel = int(data.split(',')[3])
        self.z_vel = int(data.split(',')[4])
        self.xy_slope = (self.y_vel / self.x_vel)
        self.y0 =  self.y_pos - (self.xy_slope * self.x_pos)

for idx, data in enumerate(input):
    a = Hailstone(data)
    
    for i in range(len(input) - idx - 1):
        b = Hailstone(input[i + idx + 1])

        x, y, interceptFound = getIntersect(a.xy_slope, b.xy_slope, a.y0, b.y0)

        if interceptFound:
            if inside(x, y):
                if isInFuture(a.x_vel, a.x_pos, x, a.y_vel, a.y_pos, y):
                    if isInFuture(b.x_vel, b.x_pos, x, b.y_vel, b.y_pos, y):
                        output += 1
                
print("Day 24 - Part 1: " + str(output))