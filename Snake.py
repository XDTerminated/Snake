# Import Pygame and Random
import random
import pygame

# Constants/Global Variables
GREEN1 = (170, 215, 81)
GREEN2 = (162, 209, 73)
BLUE = (70, 116, 233)
RED = (231,71,29)
HEIGHT, WIDTH = 480, 480 # Dimensions of the pygame window
FPS = 8 # Used to control the frame rate of the game. Mainly used in this game to control the speed of the snake.

SCORE = 0

# Initialize Pygame and set up Window
pygame.init() # Initializes all imported pygame modules
pygame.font.init() # Initializes the font module
MYFONT = pygame.font.SysFont('Comic Sans MS', 30) # Sets up font
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Creates a W x H Window
pygame.display.set_caption("Snake") # Title of pygame window

# Classes
class Snake(): # Creates a Snake Class to help control the snake
    # Init function to initialize the variables inside the class and the class itself
    def __init__(self):
        self.positions = [[12, 12]]
        self.direction = "East"
        self.length = 1

    # Returns the position of the snake
    def position(self):
        return self.positions

    # Resets the game if the snake touches itself or the edge
    def touchingEdgeOrSelf(self):
        self.length = 1
        self.positions = [[12, 12]]
        self.direction = "East"

    # Adds to the length and positions list when the snake eats something
    def eatFood(self):
        self.length += 1
        if self.direction == "North":
            self.positions.insert(0, [self.positions[0][0], self.positions[0][1] + 1])

        elif self.direction == "South":
            self.positions.insert(0, [self.positions[0][0], self.positions[0][1] - 1])
            

        elif self.direction == "East":
            self.positions.insert(0, [self.positions[0][0] - 1, self.positions[0][1]])
            

        elif self.direction == "West":
            self.positions.insert(0, [self.positions[0][0] + 1, self.positions[0][1]])

    # Controls the movement of the snake
    def move(self):
        if self.direction == "East":
            self.positions[0][0] = self.positions[-1][0] + 1
            self.positions[0][1] = self.positions[-1][1]
            self.positions.append(self.positions.pop(0))

        elif self.direction == "West":
            self.positions[0][0] = self.positions[-1][0] - 1
            self.positions[0][1] = self.positions[-1][1]
            self.positions.append(self.positions.pop(0))

        elif self.direction == "North":
            self.positions[0][0] = self.positions[-1][0]
            self.positions[0][1] = self.positions[-1][1] - 1
            self.positions.append(self.positions.pop(0))

        elif self.direction == "South":
            self.positions[0][0] = self.positions[-1][0]
            self.positions[0][1] = self.positions[-1][1] + 1
            self.positions.append(self.positions.pop(0))

    # Changes the heading of the snake
    def upArrow(self):
        if self.length > 1:
            if self.direction != "South":
                self.direction = "North"

        else:
            self.direction = "North"

    def rightArrow(self):
        if self.length > 1:
            if self.direction != "West":
                self.direction = "East"

        else:
            self.direction = "East"

    def downArrow(self):
        if self.length > 1:
            if self.direction != "North":
                self.direction = "South"

        else:
            self.direction = "South"

    def leftArrow(self):
        if self.length > 1:
            if self.direction != "East":
                self.direction = "West"  

        else:
            self.direction = "West"

class Food(): # Creates a class food to help control the food position
    # Iniatializes the class and variables inside the class
    def __init__(self):
        self.position = [20, 12]
    # Randomize the position of the food
    def randomize(self):
        self.position = [random.randint(2, 23), random.randint(2, 23)]

    # Resets the positions of the food if the snake dies
    def snakeDied(self):
       self.position = [20, 12]



# Functions
def drawWindow(): # Draws the game board
    # Creates a 480 x 480 window with 20 x 20 squares
    for i in range(24):
        for j in range(24):
            if (i + j) %2 == 0:
                pygame.draw.rect(WIN, GREEN1, (20*j, 20*i, 20, 20))

            else:
                pygame.draw.rect(WIN, GREEN2, (20*j, 20*i, 20, 20))

def drawSnake(): # Moves the snake and controls where the squares for the snakes are being drawn
    global SCORE
    positions = snake.position()
    foodPosition = food.position

    # Checks whether snake has eaten the food
    if foodPosition in positions:
        snake.eatFood()
        food.randomize()
        SCORE = SCORE + 1

    # Checks whether the snake touched the edge of the window or it touched it self
    if positions[-1] in positions[0:-1] or positions[-1][0] < 0 or positions[-1][0] > 23 or positions[-1][1] < 0 or positions[-1][1] > 23:
        snake.touchingEdgeOrSelf()
        food.snakeDied()
        SCORE = 0

    # Draws the snake
    for i in range(len(positions)):
        pygame.draw.rect(WIN, BLUE, ((positions[i][0] * 20) + 2.5, (positions[i][1] * 20) + 2.5, 15, 15))

    snake.move()

def drawFood(): # Draws the food on the window
    foodPosition = food.position

    pygame.draw.rect(WIN, RED, ((foodPosition[0] * 20) + 2.5, (foodPosition[1] * 20) + 2.5, 15, 15))

def main(): # Main loop of the game
    global snake, food, SCORE
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock() # Creates a clock object to control the speed of the snake
    run = True
    while run:
        clock.tick(FPS) # Frame rates per second (8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Checks if the user quit the program
                run = False
            elif event.type == pygame.KEYDOWN: # Checks which key the user clicked
                if event.key == pygame.K_LEFT:
                    snake.leftArrow()

                elif event.key == pygame.K_RIGHT:
                    snake.rightArrow()


                elif event.key == pygame.K_UP:
                    snake.upArrow()


                elif event.key == pygame.K_DOWN:
                    snake.downArrow()

        # Updating display: The position of the snake and the food
        drawWindow()
        drawSnake()
        text_surface = MYFONT.render('SCORE: ' + str(SCORE), False, (0, 0, 0))
        WIN.blit(text_surface, (0,0))
        drawFood()
        pygame.display.flip()
        
        

    pygame.quit()

if __name__ == "__main__":
    main() # Runs the mainloop