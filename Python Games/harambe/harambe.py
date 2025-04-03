import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40  # Size of each "pixel" block
PIXEL_SIZE = 2  # Even smaller pixels for finer detail
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harambe Escape")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)  # Harambe's color
DARK_BROWN = (101, 67, 33)  # For Harambe's face
RED = (255, 0, 0)      # Children's shirt
BLUE = (0, 0, 255)     # Children's pants
GREEN = (0, 255, 0)    # Zookeeper's uniform
GRAY = (169, 169, 169) # Bullet/rifle color
BEIGE = (245, 245, 220) # Skin tone for kids/zookeeper

# Pixelated shapes (larger grid: 20x20 pixels at PIXEL_SIZE=2 fits 40x40)
HARAMBE_SHAPE = [
    # Head
    (7, 1), (8, 1), (9, 1), (10, 1), (11, 1),  # Top
    (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),  # Middle
    (6, 3), (7, 3), (12, 3), (13, 3),  # Sides
    (7, 4), (8, 4), (9, 4), (10, 4), (11, 4),  # Bottom (face area)
    # Shoulders/Arms
    (4, 5), (5, 5), (6, 5), (12, 5), (13, 5), (14, 5),
    (3, 6), (4, 6), (5, 6), (13, 6), (14, 6), (15, 6),
    (3, 7), (4, 7), (14, 7), (15, 7),
    # Body
    (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8),
    (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9),
    (7, 10), (8, 10), (9, 10), (10, 10), (11, 10),
    # Legs
    (6, 11), (7, 11), (11, 11), (12, 11),
    (5, 12), (6, 12), (12, 12), (13, 12),
    (5, 13), (6, 13), (12, 13), (13, 13)
]
HARAMBE_FACE = [(8, 4), (9, 4), (10, 4)]  # Darker face pixels

CHILD_SHAPE = [
    # Head
    (8, 2), (9, 2), (10, 2),  # Hair
    (8, 3), (9, 3), (10, 3),  # Face (BEIGE)
    # Shirt (RED)
    (7, 4), (8, 4), (9, 4), (10, 4), (11, 4),
    (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5),
    (6, 6), (7, 6), (12, 6), (13, 6),  # Arms
    # Pants (BLUE)
    (8, 7), (9, 7), (10, 7),
    (8, 8), (9, 8), (10, 8),
    # Legs (BEIGE)
    (7, 9), (11, 9),
    (7, 10), (11, 10)
]

ZOOKEEPER_SHAPE = [
    # Hat
    (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
    # Head
    (8, 1), (9, 1), (10, 1),  # Face (BEIGE)
    # Uniform (GREEN)
    (7, 2), (8, 2), (9, 2), (10, 2), (11, 2),
    (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
    (5, 4), (6, 4), (7, 4), (12, 4), (13, 4),  # Arms
    # Rifle (GRAY)
    (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4),
    # Pants (GREEN)
    (8, 5), (9, 5), (10, 5),
    (8, 6), (9, 6), (10, 6),
    # Legs (BEIGE)
    (7, 7), (11, 7)
]

BULLET_SHAPE = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0)  # Slightly longer bullet
]

# Function to reset game state
def reset_game():
    global harambe_x, harambe_y, children, zookeeper_active, bullet_x, bullet_y, bullet_active, game_over
    harambe_x, harambe_y = WIDTH // 2, HEIGHT // 2
    children = []
    for _ in range(NUM_CHILDREN):
        children.append([random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE])
    zookeeper_active = False
    bullet_x, bullet_y = 0, 0
    bullet_active = False
    game_over = False

# Initial game state
NUM_CHILDREN = 8  # Increased to 8 kids
ZOOKEEPER_X, ZOOKEEPER_Y = 0, HEIGHT // 2 - GRID_SIZE // 2
reset_game()

# Game loop
clock = pygame.time.Clock()
running = True

def draw_shape(surface, x, y, shape, color, extra_colors=None):
    """Draw a pixelated shape with multiple extra colors for specific pixels."""
    for px, py in shape:
        col = color
        if extra_colors:
            for extra_col, coords in extra_colors.items():
                if (px, py) in coords:
                    col = extra_col
                    break
        pygame.draw.rect(surface, col, (x + px * PIXEL_SIZE, y + py * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif game_over and event.key == pygame.K_y:
                reset_game()
            elif game_over and event.key == pygame.K_n:
                running = False

    if not game_over:
        # Move Harambe with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and harambe_x > GRID_SIZE:
            harambe_x -= GRID_SIZE
        if keys[pygame.K_RIGHT] and harambe_x < WIDTH - GRID_SIZE:
            harambe_x += GRID_SIZE
        if keys[pygame.K_UP] and harambe_y > 0:
            harambe_y -= GRID_SIZE
        if keys[pygame.K_DOWN] and harambe_y < HEIGHT - GRID_SIZE:
            harambe_y += GRID_SIZE

        # Check for collision with children
        harambe_rect = pygame.Rect(harambe_x, harambe_y, GRID_SIZE, GRID_SIZE)
        for child in children:
            child_rect = pygame.Rect(child[0], child[1], GRID_SIZE, GRID_SIZE)
            if harambe_rect.colliderect(child_rect) and not bullet_active:
                zookeeper_active = True
                bullet_active = True
                bullet_x = ZOOKEEPER_X + GRID_SIZE
                bullet_y = harambe_y + GRID_SIZE // 2 - PIXEL_SIZE
                break

        # Move children randomly
        for child in children:
            move = random.choice(["left", "right", "up", "down", "stay"])
            if move == "left" and child[0] > GRID_SIZE:
                child[0] -= GRID_SIZE
            elif move == "right" and child[0] < WIDTH - GRID_SIZE:
                child[0] += GRID_SIZE
            elif move == "up" and child[1] > 0:
                child[1] -= GRID_SIZE
            elif move == "down" and child[1] < HEIGHT - GRID_SIZE:
                child[1] += GRID_SIZE

        # Move bullet if active
        if bullet_active:
            bullet_x += 30
            bullet_rect = pygame.Rect(bullet_x, bullet_y, PIXEL_SIZE * 5, PIXEL_SIZE)
            if bullet_rect.colliderect(harambe_rect):
                game_over = True
            elif bullet_x > WIDTH:
                bullet_active = False

    # Draw everything
    screen.fill(BLACK)

    # Draw Harambe
    draw_shape(screen, harambe_x, harambe_y, HARAMBE_SHAPE, BROWN, {DARK_BROWN: HARAMBE_FACE})

    # Draw children
    for child in children:
        draw_shape(screen, child[0], child[1], CHILD_SHAPE, RED, {BEIGE: [(8, 3), (9, 3), (10, 3), (7, 9), (11, 9), (7, 10), (11, 10)], BLUE: [(8, 7), (9, 7), (10, 7), (8, 8), (9, 8), (10, 8)]})

    # Draw zookeeper
    draw_shape(screen, ZOOKEEPER_X, ZOOKEEPER_Y, ZOOKEEPER_SHAPE, GREEN, {BEIGE: [(8, 1), (9, 1), (10, 1), (7, 7), (11, 7)], GRAY: [(11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4)]})

    # Draw bullet if active
    if bullet_active:
        draw_shape(screen, bullet_x, bullet_y, BULLET_SHAPE, GRAY)

    # Display game over message and play again prompt
    if game_over:
        font = pygame.font.SysFont(None, 48)
        game_over_text = font.render("Zookeeper Shot Harambe!", True, WHITE)
        play_again_text = font.render("Play Again? (Y/N)", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 48))
        screen.blit(play_again_text, (WIDTH // 2 - 100, HEIGHT // 2 + 8))

    # Update display
    pygame.display.flip()
    clock.tick(15)

# Quit Pygame
pygame.quit()
