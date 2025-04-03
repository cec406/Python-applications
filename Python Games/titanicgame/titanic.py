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
ICEBERG_WIDTH = 160
ICEBERG_HEIGHT = 80
SHIP_SPEED = 5
INITIAL_ICEBERG_SPEED = 5
SPEED_INCREMENT = 0.01

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Titanic Avoid Icebergs")

# Load images
ship_img = pygame.image.load("titanic.png")
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
iceberg_img = pygame.image.load("iceberg.png")
iceberg_img = pygame.transform.scale(iceberg_img, (ICEBERG_WIDTH, ICEBERG_HEIGHT))

# Iceberg class
class Iceberg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = iceberg_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(100, SCREEN_HEIGHT - ICEBERG_HEIGHT - 100)
    
    def update(self):
        global ICEBERG_SPEED
        self.rect.x -= ICEBERG_SPEED
        if self.rect.x < -ICEBERG_WIDTH:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(100, SCREEN_HEIGHT - ICEBERG_HEIGHT - 100)

# Titanic class
class Titanic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= SHIP_SPEED
        if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - SHIP_HEIGHT:
            self.rect.y += SHIP_SPEED

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
    
    while True:
        screen.fill(WHITE)
        y_offset = SCREEN_HEIGHT // 3
        for line in game_over_texts:
            screen.blit(line, (20, y_offset))
            y_offset += 40
        
        screen.blit(score_text, (20, y_offset))
        y_offset += 40
        screen.blit(fact_text, (20, y_offset))
        y_offset += 40
        screen.blit(restart_text, (20, y_offset))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False

# Function to initialize game state
def init_game():
    global ICEBERG_SPEED, all_sprites, icebergs, ship
    ICEBERG_SPEED = INITIAL_ICEBERG_SPEED
    all_sprites = pygame.sprite.Group()
    icebergs = pygame.sprite.Group()
    ship = Titanic()
    all_sprites.add(ship)
    for _ in range(5):
        iceberg = Iceberg()
        all_sprites.add(iceberg)
        icebergs.add(iceberg)

# Main game function
def main():
    global ICEBERG_SPEED
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Initialize game state
        init_game()
        score = 0
        game_running = True
        
        # Game loop
        while game_running:
            screen.fill(BLUE)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            # Update all sprites
            all_sprites.update()

            # Increase score over time
            score += 1

            # Increase iceberg speed over time
            ICEBERG_SPEED += SPEED_INCREMENT

            # Check for collisions
            if pygame.sprite.spritecollideany(ship, icebergs):
                message = random.choice([
                    "The Titanic collided with the iceberg. Over 1,500 souls were lost.",
                    "Iceberg impact! The icy waters claimed more lives than anyone imagined.",
                    "Disaster struck! The ship is sinking!",
                    "The ship is sinking! Thousands perished in the freezing sea.",
                    "The Titanic has met its doom! A catastrophe that changed history forever.",
                    "Tragedy unfolds! The Titanic disappears beneath the waves.",
                    "An unimaginable disaster! The mighty ship lost to the ocean forever."
                ])
                if not game_over(message, score):
                    running = False
                game_running = False
            
            # Draw all sprites
            all_sprites.draw(screen)
            
            # Display the score
            display_score(score)
            
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()