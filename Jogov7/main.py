import sys, intro
from config import *

pygame.init()
clock = pygame.time.Clock

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        intro.run()
    clock.tick(120)
