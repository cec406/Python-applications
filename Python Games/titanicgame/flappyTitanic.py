import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game settings
SHIP_WIDTH = 100
SHIP_HEIGHT = 60
SHIP_FLAP = -10
GRAVITY = 1
ICEBERG_WIDTH = 160
ICEBERG_HEIGHT = 80
ICEBERG_SPEED = 5
ICEBERG_GAP = 300

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Titanic")

# Load images
ship_img = pygame.image.load("titanic.png")
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
iceberg_img = pygame.image.load("iceberg.png")
iceberg_img = pygame.transform.scale(iceberg_img, (ICEBERG_WIDTH, ICEBERG_HEIGHT))
captain_img = pygame.image.load("captain.png")  # Load captain image
captain_img = pygame.transform.scale(captain_img, (200, 200))  # Resize appropriately

# Iceberg class
class Iceberg(pygame.sprite.Sprite):
    def __init__(self, x_offset):
        super().__init__()
        self.image = iceberg_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + x_offset
        self.rect.y = random.randint(100, SCREEN_HEIGHT - ICEBERG_HEIGHT - 100)
    
    def update(self):
        self.rect.x -= ICEBERG_SPEED
        if self.rect.x < -ICEBERG_WIDTH:
            self.rect.x = SCREEN_WIDTH + ICEBERG_GAP
            self.rect.y = random.randint(100, SCREEN_HEIGHT - ICEBERG_HEIGHT - 100)

# Titanic class
class Titanic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0
    
    def update(self):
        self.velocity += GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.velocity = SHIP_FLAP
        self.rect.y += self.velocity
        if self.rect.y >= SCREEN_HEIGHT - SHIP_HEIGHT:  # Detect collision with bottom
            self.rect.y = SCREEN_HEIGHT - SHIP_HEIGHT

# Function to display score
def display_score(score):
    font = pygame.font.SysFont('Arial', 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

# Function to wrap text for game over messages
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_width, _ = font.size(test_line)
        
        if test_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

# Function to display game over message
def game_over(message, score):
    font = pygame.font.SysFont('Arial', 30)
    restart_font = pygame.font.SysFont('Arial', 24)
    
    wrapped_message = wrap_text(message, font, SCREEN_WIDTH - 40)
    game_over_texts = [font.render(line, True, BLACK) for line in wrapped_message]
    
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    restart_text = restart_font.render("Press R to restart or Q to quit.", True, BLACK)
    
    fact = random.choice([
        "Did you know? The Titanic had four smokestacks, but only three worked.",
        "Fun fact: The Titanic was carrying over 2,200 passengers and crew.",
        "Did you know? The Titanic's distress signal was sent via wireless radio.",
        "Fun fact: Over 700 survivors were rescued by the Carpathia.",
        "Did you know? The Titanic was the largest ship ever built at the time.",
        "Fun fact: The Titanic had a swimming pool and a gym on board.",
        "Did you know? The Titanic's wreck was discovered in 1985, 73 years after it sank.",
        "Fun fact: The Titanic used over 600 tons of coal per day.",
        "Did you know? The ship broke into two pieces before sinking completely.",
        "Fun fact: There were only enough lifeboats for about half of the passengers."
    ])
    fact_text = font.render(fact, True, BLACK)
    
    y_offset = SCREEN_HEIGHT // 3
    screen.fill(WHITE)
    screen.blit(captain_img, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 250))  # Display captain image
    for line in game_over_texts:
        screen.blit(line, (20, y_offset))
        y_offset += 40
    
    screen.blit(score_text, (20, y_offset))
    y_offset += 40
    screen.blit(fact_text, (20, y_offset))
    y_offset += 40
    screen.blit(restart_text, (20, y_offset))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    return False

def main_game_loop():
    # Initialize sprites
    all_sprites = pygame.sprite.Group()
    icebergs = pygame.sprite.Group()
    ship = Titanic()
    all_sprites.add(ship)
    for i in range(5):
        iceberg = Iceberg(i * ICEBERG_GAP)
        all_sprites.add(iceberg)
        icebergs.add(iceberg)

    # Game loop
    running = True
    clock = pygame.time.Clock()
    score = 0
    while running:
        screen.fill(BLUE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all sprites
        all_sprites.update()

        # Increase score over time
        score += 1

        # Check for collisions
        if pygame.sprite.spritecollideany(ship, icebergs) or ship.rect.y >= SCREEN_HEIGHT - SHIP_HEIGHT:
            message = random.choice([
                "The Titanic collided with the iceberg. Over 1,500 souls were lost.",
                "Iceberg impact! The icy waters claimed more lives than anyone imagined.",
                "Disaster struck! The ship is sinking!"
            ])
            running = game_over(message, score)
            score = 0
            if running:
                main_game_loop()
            else:
                break
        
        all_sprites.draw(screen)
        display_score(score)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_game_loop()