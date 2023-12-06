import pygame
import random

WINDOW_SIZE = 800

def gen(num):
    return set([(random.randrange(0, WINDOW_SIZE), random.randrange(0, WINDOW_SIZE)) for _ in range(num)])


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
