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
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.width)

class PoopParticle(gameObject):
    def __init__(self, x, y, width, height, color, mass=1):
        super().__init__(x, y, width, height, color)
        self.vx = 0  # Velocity in x direction
        self.vy = 0  # Velocity in y direction
        self.mass = mass

    def update_position(self):
        self.x += self.vx
        self.y += self.vy

class Mouse(gameObject):
    def __init__(self, x, y, width, height, color, age, dna, speed, belly):
        super().__init__(x, y, width, height, color)
        self.age = age
        self.dna = dna
        self.speed = speed
        self.belly = belly
    def draw(self, surface):
        pygame.draw.circle(surface, addColors(self.color,self.dna.color_variation),(int(self.x), int(self.y)), self.dna.size_variation + int(self.width / 2))
    def makePoop(self, width, height):
        return PoopParticle(self.x, self.y, 5, 5, (165, 42, 42), mass=random.uniform(0.5, 1.5))
    def eat(self,cheese):
        self.belly += 1
        cheese.width -= 1
        cheese.height -= 1


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
    width = 30
    height = 30
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
    speed = random.uniform(3, 12)  # Example speed range
    belly = 0  # Example initial belly value
    return Mouse(x, y, width, height, color, age, dna, speed, belly)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculateDistance(obj1, obj2):
    return distance(obj1.x, obj1.y, obj2.x, obj2.y)   

def nearestObject(obj1, objects):
    temp_dist = 99999
    closest = Cheese(999999,9999999,1,1,(0,0,0),0)
    for item in objects:
        if calculateDistance(obj1, item) < temp_dist:
            closest = item
            temp_dist = calculateDistance(obj1, item)
    return objects.index(closest)

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
        obj1.x, obj1.y = x2, y2
    
    obj1.x, obj1.y = new_x, new_y

def addColors(color1, color2):
    r = min(color1[0] + color2[0], 255)
    g = min(color1[1] + color2[1], 255)
    b = min(color1[2] + color2[2], 255)
    return (r, g, b)
def apply_gravity(poops, G=6.67430e-11, scale=1e10):
    for i, poop1 in enumerate(poops):
        if isinstance(poop1, PoopParticle):  # Only apply gravity to PoopParticle objects
            fx = 0
            fy = 0
            for j, poop2 in enumerate(poops):
                if i != j and isinstance(poop2, PoopParticle):
                    dx = poop2.x - poop1.x
                    dy = poop2.y - poop1.y
                    d = math.sqrt(dx*dx + dy*dy)
                    if d > 0:
                        F = G * poop1.mass * poop2.mass / (d*d)
                        F *= scale  # Scale up the force for visual effect
                        fx += (F * dx / d)
                        fy += (F * dy / d)
            
            # Apply acceleration (F = ma)
            ax = fx / poop1.mass
            ay = fy / poop1.mass

            speed_limit = .004
            if abs(ax) > speed_limit: 
                poop1.vx += sign(ax) * speed_limit
            else:
                poop1.vx += ax
            if abs(ay) > speed_limit:
                poop1.vy += sign(ay) * speed_limit
            else:
                poop1.vy += ay

    # Update positions
    for poop in poops:
        if isinstance(poop, PoopParticle):
            poop.update_position()

def sign(x):
    return math.copysign(1, x)

def makeClumps(poops,cheeses):
    for i,poop in enumerate(poops):
        qualified = withinRange(poop,poops,50)
        if len(qualified) > 7:
            print("MORPHED!")
            cheeses.append(Cheese(poop.x,poop.y,30,30,(255,255,0),0))
            for i in sorted(qualified,reverse=True):
                poops.pop(i)
    return poops,cheeses

def withinRange(poop, poops, r):
    qualified = []
    for testPoop in poops:
        if abs(poop.x - testPoop.x) < r and abs(poop.y - testPoop.y) < r:
            qualified.append(poops.index(testPoop))
    return qualified#,maxDistance








