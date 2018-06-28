import random
import pygame
from pygame.locals import *


class BackgroundStars:
    def __init__(self):
        self.width = 128
        self.height = 128
        self.tile_size = 256
        self.tiles = []
        for x in range(self.width):
            self.tiles.append([])
            for y in range(self.height):
                stars = []
                for i in range(random.randint(1, 3)):
                    stars.append(self.generate_star())
                self.tiles[x].append(stars)

    def generate_star(self):
        pos_x = random.randint(0, self.tile_size)
        pos_y = random.randint(0, self.tile_size)
        color = (255, random.randint(192, 255), random.randint(128, 255))
        return (pos_x, pos_y, color)
    
    def update(self, screen_size, camera):
        pass
    
    def draw(self, screen, camera):
        screen_width, screen_height = screen.get_size()
        left =   (int(camera.pos.x)) // self.tile_size
        top =    (int(camera.pos.y)) // self.tile_size
        right =  (int(camera.pos.x) + screen_width)  // self.tile_size + 1
        bottom = (int(camera.pos.y) + screen_height) // self.tile_size + 1
        for x in range(left, right):
            for y in range(top, bottom):
                ix = x % self.width
                iy = y % self.height
                for star in self.tiles[ix][iy]:
                    pos_x, pos_y, color = star
                    pix_x = x * self.tile_size + pos_x
                    pix_y = y * self.tile_size + pos_y
                    pix_screen_pos = camera.apply((pix_x, pix_y))
                    pix_x, pix_y = int(pix_screen_pos.x), int(pix_screen_pos.y)
                    screen.set_at((pix_x, pix_y), color)


