import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, target):
        if pygame.sprite.collide_rect(self, target):
            target.health -= 10

# Create player instances
player1 = Player(RED, 100, SCREEN_HEIGHT - 100)
player2 = Player(BLUE, SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_a]:
        player1.move(-5, 0)
    if keys[pygame.K_d]:
        player1.move(5, 0)
    if keys[pygame.K_w]:
        player1.move(0, -5)
    if keys[pygame.K_s]:
        player1.move(0, 5)
    if keys[pygame.K_SPACE]:
        player1.attack(player2)

    # Player 2 controls
    if keys[pygame.K_LEFT]:
        player2.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player2.move(5, 0)
    if keys[pygame.K_UP]:
        player2.move(0, -5)
    if keys[pygame.K_DOWN]:
        player2.move(0, 5)
    if keys[pygame.K_RETURN]:
        player2.attack(player1)

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Draw health bars
    pygame.draw.rect(screen, RED, [10, 10, player1.health * 2, 20])
    pygame.draw.rect(screen, BLUE, [SCREEN_WIDTH - 210, 10, player2.health * 2, 20])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
