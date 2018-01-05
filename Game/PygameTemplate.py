import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (700, 500) #width = 700, height = 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Box")

done = False
clock = pygame.time.Clock()

rect_x = 0
rect_y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    ##pygame.draw.rect(screen, RED, [rect_x, 50, 50, 50])
    a = 10 ##speed
    if rect_x < size[0] - 50 and rect_y == 0:
        pygame.draw.ellipse(screen, GREEN, [rect_x, rect_y, 50, 50])
        rect_x += a

        pygame.display.flip()
        clock.tick(60)
    elif rect_x == size[0] - 50 and rect_y < size[1] - 50:
        pygame.draw.ellipse(screen, GREEN, [rect_x, rect_y, 50, 50])
        rect_y += a

        pygame.display.flip()
        clock.tick(60)

    elif rect_y == size[1] - 50 and rect_x > 0 :
        pygame.draw.ellipse(screen, GREEN, [rect_x, rect_y, 50, 50])
        rect_x -= a

        pygame.display.flip()
        clock.tick(60)

    elif rect_x == 0 and rect_y > 0 :
        pygame.draw.ellipse(screen, GREEN, [rect_x, rect_y, 50, 50])
        rect_y -= a

        pygame.display.flip()
        clock.tick(60)


pygame.quit()