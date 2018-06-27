#! python3

import pygame
import os


_images = {}
_sounds = {}


def canonicalize_path(path):
    return path.replace('/', os.sep).replace('\\', os.sep)


def get_image(path):
    global _images
    image = _images.get(path)
    if image is None:
        canonicalized_path = canonicalize_path(path)
        try:
            image = pygame.image.load(canonicalized_path)
            image = image.convert_alpha()
        except pygame.error as e:
            print("Warning: Couldn't load " + path + ": " + format(e))
            image = pygame.Surface((0,0))
        _images[path] = image
    return image


class EmptySound:
    def play(self): pass
    def stop(self): pass
    def fadeout(seld): pass
    def set_volume(self, v): pass
    def get_volume(self): return 0
    def get_num_channels(self): return 0
    def get_length(self): return 0


def get_sound(path):
    global _sounds
    sound = _sounds.get(path)
    if sound is None:
        canonicalized_path = canonicalize_path(path)
        try:
            sound = pygame.mixer.Sound(canonicalized_path)
        except pygame.error as e:
            print("Warning: Culdn't load " + path + ": " + format(e))
            sound = EmptySound()
        _sounds[path] = sound
    return sound


