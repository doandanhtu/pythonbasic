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
angle = 0
rect_x = 200
rect_y = 100
def placeCar(x, y):
    screen.blit(carImg, (x, y))

def rotateCar(x, y, angle):
    rotatedCar = pygame.transform.rotate(carImg, angle)
    rot_rect = rotatedCar.get_rect(center=(x, y))
    screen.blit(rotatedCar, (rot_rect.left, rot_rect.top))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle += 5
            elif event.key == pygame.K_LEFT:
                angle -= 5
            elif event.key == pygame.K_UP:
                rect_x += 5
            elif event.key == pygame.K_DOWN:
                rect_x -= 5


    screen.fill(WHITE)
    #placeCar(100, 200)
    if angle > 360:
        angle = 0
    if angle < 0:
        angle = 360

    rotateCar(rect_x, rect_y, angle)
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()