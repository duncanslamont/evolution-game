


class map:
    def __init__(self,width,height,mice,cheeses,poops,window):
        self.width = width
        self.height = height
        self.mouses = mouses
        self.cheeses = cheeses
        self.window = pygame.display.set_mode((self.width, self.height))
    def draw():
        self.window.fill((0,0,0))  # Fill the background with black
        
        for mouse in mice:
            mouse.draw(self.window)
        for cheese in cheeses:
            cheese.draw(self.window)
        for poop in poops:
            poop.draw(self.window)


def updateGameState(map,tick):
    print("test")



def initiateMapVersionOne(width,height):
    print("")
