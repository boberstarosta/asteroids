#!/usr/bin/env python3

import pygame
from pygame.locals import *

import sprites


# ======================= Game class: =======================

class Game:
	SCREEN_W, SCREEN_H = SCREEN_SIZE = 1280, 960
	FPS = 60
	MOUSE_VISIBLE = True
	BACKGROUND_COLOR = (0,0,0)

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
		self.clock = pygame.time.Clock()
		pygame.mouse.set_visible(self.MOUSE_VISIBLE)
		pygame.display.set_caption("asteroids")
	
		self.player_ship = sprites.PlayerShip()
	
	def handle_event(self, event):
		if event.type == QUIT:
			self.quit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			self.quit()
	
	def update(self):
		self.player_ship.update()
	
	def draw(self, screen):
		self.player_ship.draw(screen)
	
	def run(self):
		self.running = True
		
		while self.running:
			for event in pygame.event.get():
				self.handle_event(event)
			self.update()
			self.screen.fill(self.BACKGROUND_COLOR)
			self.draw(self.screen)
			pygame.display.flip()
			self.clock.tick(self.FPS)
	
	def quit(self):
		self.running = False

		
# =======================================

if __name__ == "__main__":
	info = """Controls:
	  LEFT/RIGHT  - rotate
	  SPACE       - kill rotation
	  UP          - accelerate
	"""
	print(info)
	Game().run()


