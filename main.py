import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
TILE_CLR = (128,128,255)
YELLOW = (255, 255, 0)

WINDOW_SIZE = 800
TILE_SIZE = 20
GRID_SIZE = (WINDOW_SIZE/TILE_SIZE)
FPS = 60

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, WINDOW_SIZE), random.randrange(0, WINDOW_SIZE)) for _ in range(num)])

def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))


    for row in range(WINDOW_SIZE):
        pygame.draw.line(screen, WHITE, (0, row*TILE_SIZE), (WINDOW_SIZE, row*TILE_SIZE))

    for col in range(WINDOW_SIZE):
        pygame.draw.line(screen, WHITE, (col * TILE_SIZE, 0), (col * TILE_SIZE, WINDOW_SIZE))


def adjust_grid(positions):
    all_neighbours = set()
    new_positions = set()

    for position in positions:
        neighbours = get_neighbours(position)
        all_neighbours.update(neighbours)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbours:
        neighbours = get_neighbours(position)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbours(pos):
    x, y = pos
    neighbours = []

    for dx in [-1,0,1]:
        if x + dx < 0 or x + dx > WINDOW_SIZE:
            continue
        for dy in [-1, 0, 1]:
            if y+ dy < 0 or y+dy > WINDOW_SIZE:
                continue 

            if dx == 0 and dy == 0:
                continue
                
            neighbours.append((x+dx, y+dy))

    return neighbours


def main():
    running = True
    playing = False
    count = 0
    update_freq = 120

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
        draw_grid(positions)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()