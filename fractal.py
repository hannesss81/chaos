import random
import math
import matplotlib.pyplot as plt

p1 = [[0,0,0,0.25,0,-0.4,0.02],
[0.95,0.005,-0.005,0.93,-0.002,0.5,0.84],
[0.035,-0.2,0.16,0.04,-0.09,0.02,0.07],
[-0.04,0.2,0.16,0.04,0.083,0.12,0.07]]

p2 = [[0,0,0,0.16,0,0,0.01],
[0.85,0.04,-0.04,0.85,0,1.6,0.85],
[0.2,-0.26,0.23,0.22,0,1.6,0.07],
[-0.15,0.28,0.26,0.24,0,0.44,0.07]]

def drawFern(p, n):
    x, y = 0, 0
    x_coords, y_coords = [], []

    f1, f2, f3, f4 = p[0], p[1], p[2], p[3]

    for i in range(n):
            rand = random.random()
            if rand < f1[6]:
                    x = f1[0]*x + f1[1]*y + f1[4]
                    y = f1[2]*x + f1[3]*y + f1[5]
            elif  rand <= f1[6]+f2[6]:
                    x = f2[0]*x + f2[1]*y + f2[4]
                    y = f2[2]*x + f2[3]*y + f2[5]
            elif rand <= f1[6]+f2[6]+f3[6]:
                    x = f3[0]*x + f3[1]*y + f3[4]
                    y = f3[2]*x + f3[3]*y + f3[5]
            else:
                    x = f4[0]*x + f4[1]*y + f4[4]
                    y = f4[2]*x + f4[3]*y + f4[5]
            x_coords.append(x*1000)
            y_coords.append(y*1000)

    plt.figure(figsize=(6,9))
    plt.scatter(x_coords, y_coords, s=0.1, color="green")

    while True:
        plt.pause(0.05)

def drawSierpinski(n):
    r,g,b = (0,0), (0,10), (5,8)
    loc = (0,0)

    x_coords, y_coords = [], []

    for i in range(n):
        rand = random.random()
        if rand < 0.33:
            loc = getNewSierpinskiLoc(r, loc)
        elif rand < 0.66:
            loc = getNewSierpinskiLoc(g, loc)
        else:
            loc = getNewSierpinskiLoc(b, loc)
        x_coords.append(loc[0])
        y_coords.append(loc[1])

    plt.figure(figsize=(10,10))
    plt.scatter(x_coords, y_coords, s=0.3, color="green")

    while True:
        plt.pause(0.05)

def getPolygon(n):
    vertices = []
    radian_segment = math.pi * 2 / n
    for i in range(n):
        vertices.append((math.sin(radian_segment*i), math.cos(radian_segment*i)))
    return vertices

def getNewSierpinskiLoc(vertice, loc, div=2):
    return (vertice[0]-loc[0])/div, (vertice[1]-loc[1])/div

def drawChaosGame(length, n):
    vertices = getPolygon(n)
    loc = (0,0)

    last = None
    x_coords, y_coords = [], []

    for i in range(length):
        cur = random.choice(vertices)
        loc = getNewSierpinskiLoc(cur, loc, 2)

        if cur != last:
            x_coords.append(loc[0])
            y_coords.append(loc[1])
        last = cur


    plt.figure(figsize=(10,10))
    plt.scatter(x_coords, y_coords, s=0.1, color="green")

    while True:
        plt.pause(0.05)



drawChaosGame(100000, 3) # pentagon
drawSierpinski(10000)
drawFern(p2, 15000)
