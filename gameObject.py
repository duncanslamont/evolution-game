import math
import random
from dna import *
import pygame

class gameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

class Mouse(gameObject):
    def __init__(self, x, y, width, height, color, age, dna, speed, belly):
        super().__init__(x, y, width, height, color)
        self.age = age
        self.dna = dna
        self.speed = speed
        self.belly = belly

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.width / 2))

class Cheese(gameObject):
    def __init__(self, x, y, width, height, color, age):
        super().__init__(x, y, width, height, color)
        self.age = age
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (int(self.x), int(self.y), self.width, self.height))
# Function to create a random Cheese object
def makeRandomCheese(screen_width, screen_height):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    color = (255, 255, 0)  # Yellow
    width = 10
    height = 10
    age = 0
    return Cheese(x, y, width, height, color, age)

# Function to create a random Mouse object
def makeRandomMouse(screen_width, screen_height):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    color = (128, 128, 128)  # Gray
    width = 10
    height = 10
    age = 0
    dna = makeRandomDNA()
    speed = random.uniform(5, 15)  # Example speed range
    belly = 0  # Example initial belly value
    return Mouse(x, y, width, height, color, age, dna, speed, belly)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculateDistance(obj1, obj2):
    return distance(obj1.x, obj1.y, obj2.x, obj2.y)   

def nearestObject(obj1, objects):
    temp_dist = 99999
    closest = obj1
    for item in objects:
        if calculateDistance(obj1, item) < temp_dist:
            closest = item
            temp_dist = calculateDistance(obj1, item)
    return closest

def moveCloser(obj1, obj2, step):
    x1, y1 = obj1.x, obj1.y
    x2, y2 = obj2.x, obj2.y

    # Calculate the distance between the two points
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # If already at the target, return the same position
    if dist == 0:
        return (x1, y1)
    
    # Calculate the direction vector and normalize it
    direction_x = (x2 - x1) / dist
    direction_y = (y2 - y1) / dist
    
    # Calculate the new position by moving `step` closer
    new_x = x1 + direction_x * step
    new_y = y1 + direction_y * step
    
    if abs(new_x - x2) < step and abs(new_y - y2) < step:
        return (x2, y2)
    
    obj1.x, obj1.y = new_x, new_y

def addColors(color1, color2):
    r = min(color1[0] + color2[0], 255)
    g = min(color1[1] + color2[1], 255)
    b = min(color1[2] + color2[2], 255)
    return (r, g, b)

