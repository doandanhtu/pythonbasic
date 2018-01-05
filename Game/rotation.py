import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Load Image")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')

def placeCar(x, y):
    screen.blit(carImg, (x, y))

def rotateCar(x, y, angle):
    rotatedCar = pygame.transform.rotate(carImg, angle)
    screen.blit(rotatedCar, (x, y))

# -------- Main Program Loop -----------

angle = 0
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(WHITE)
    placeCar(400, 300)
    #rotateCar(50, 100, angle)
    #angle += 1
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()