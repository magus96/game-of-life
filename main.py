import pygame
import random
from grid_helpers import draw_grid, adjust_grid
from utils import gen, get_neighbours

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
TILE_CLR = (128,128,255)
YELLOW = (255, 255, 0)

WINDOW_SIZE = 800
TILE_SIZE = 20
GRID_SIZE = (WINDOW_SIZE/TILE_SIZE)
FPS = 180

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

clock = pygame.time.Clock()

def main():
    running = True
    playing = False
    count = 0
    update_freq = 2 * FPS

    positions = set()
    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    playing = not playing

                if key == pygame.K_ESCAPE:
                    pygame.quit()

                if key == pygame.K_r:
                    positions = set()
                    playing = False

                if key == pygame.K_g:
                    positions = gen(random.randrange(150, 200) * WINDOW_SIZE)
    
        screen.fill(TILE_CLR)
        draw_grid(positions, screen= screen)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()