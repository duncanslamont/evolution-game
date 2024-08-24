from gameObject import gameObject
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculateDistance(object_1,object_2):
    return distance(object_1.x,object_1.y,object_2.x,object_2.y)
