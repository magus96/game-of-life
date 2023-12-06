import pygame

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

WINDOW_SIZE = 800
TILE_SIZE = 20
GRID_SIZE = (WINDOW_SIZE/TILE_SIZE)
FPS = 180

def draw_grid(positions, screen):
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