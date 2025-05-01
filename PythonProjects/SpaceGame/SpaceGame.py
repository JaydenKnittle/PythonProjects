import pygame
import time
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Background image
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

# Player settings
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 100
PLAYER_VEL = 7

# Star settings
STAR_WIDTH = 30
STAR_HEIGHT = 30
STAR_VEL = 5

# Font settings
FONT = pygame.font.SysFont("comicsans", 30)

# Load player sprite
player_img = pygame.transform.scale(pygame.image.load("player.jpg"), (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load star sprite
star_img = pygame.transform.scale(pygame.image.load("star.jpg"), (STAR_WIDTH, STAR_HEIGHT))

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    # Display elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    # Draw player sprite
    WIN.blit(player_img, (player.x, player.y))

    # Draw star sprites
    for star in stars:
        WIN.blit(star_img, (star.x, star.y))

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 20, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    stars = []
    star_spawn_delay = 1000  # milliseconds
    last_star_spawn = pygame.time.get_ticks()

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width < WIDTH:
            player.x += PLAYER_VEL

        # Spawn stars
        now = pygame.time.get_ticks()
        if now - last_star_spawn > star_spawn_delay:
            last_star_spawn = now
            star_x = random.randint(0, WIDTH - STAR_WIDTH)
            star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
            stars.append(star)

        # Move stars and remove off-screen stars
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)

        # Check collision between player and stars
        for star in stars:
            if player.colliderect(star):
                run = False  # Game over if player collides with a star

        # Draw everything
        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()
