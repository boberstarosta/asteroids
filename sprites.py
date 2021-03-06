import pygame
from vector import Vec2
import content


class RotatingSprite(pygame.sprite.Sprite):
    def __init__(self, image,
                 position=Vec2(0,0), velocity=Vec2(0,0),
                 rotation=0.0, angular_velocity=0.0):
        super().__init__()
        
        self.original_img = image
        self.rect = self.original_img.get_rect()
        
        self.position = position
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.rotation = rotation
    
    def update(self):
        # Update position and rotation
        self.position += self.velocity
        self.rotation += self.angular_velocity
        while self.rotation < 0:
            self.rotation += 360.0
        while self.rotation >= 360.0:
            self.rotation -= 360.0
    
        # Update sprite image with rotated original_image
        self.image = pygame.transform.rotate(self.original_img, -self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = tuple(self.position)
    
    def draw(self, screen, camera):
        screen.blit(self.image,  camera.apply_rect(self.rect))


class PlayerShip(RotatingSprite):
    def __init__(self, position=Vec2(200,100)):
        super().__init__(image=content.get_image("data/ship01.png"),
                         position=position)
        
        self.angular_acceleration = 0.1
        self.max_angular_velocity = 120.0 * self.angular_acceleration
        self.acceleration = 0.1
    
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_LEFT]:  # rotate left
            self.angular_velocity -= self.angular_acceleration
        elif keys_pressed[pygame.K_RIGHT]:  # rotate right
            self.angular_velocity += self.angular_acceleration
        else:
            if self.angular_velocity < 0:
                self.angular_velocity += self.angular_acceleration
            elif self.angular_velocity > 0:
                self.angular_velocity -= self.angular_acceleration
        
        if abs(self.angular_velocity) < self.angular_acceleration:
            self.angular_velocity = 0.0
        self.angular_velocity = max(-self.max_angular_velocity,
            min(self.max_angular_velocity, self.angular_velocity))
        
        if keys_pressed[pygame.K_UP]:  # fire engine
            direction = Vec2.FromAngleX(self.rotation)
            self.velocity += direction * self.acceleration
        
        super().update()

