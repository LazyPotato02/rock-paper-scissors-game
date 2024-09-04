import pygame
import sys
import random

score = 0
score_increment = 1
# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")

rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Resize images if necessary
button_size = (150, 150)
rock_img = pygame.transform.scale(rock_img, button_size)
paper_img = pygame.transform.scale(paper_img, button_size)
scissors_img = pygame.transform.scale(scissors_img, button_size)

# Set positions for images at the bottom of the screen
padding = 50
button_spacing = 100

rock_rect = rock_img.get_rect(center=(screen_width // 4, screen_height - padding))
paper_rect = paper_img.get_rect(center=(screen_width // 2, screen_height - padding))
scissors_rect = scissors_img.get_rect(center=(3 * screen_width // 4, screen_height - padding))

quit_button = pygame.Rect(screen_width - 120, screen_height - 60, 100, 40)
font = pygame.font.SysFont(None, 40)
quit_text = font.render("Quit", True, (255, 255, 255))


def choose_random_option():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)


# Main loop
running = True
while running:
    selection = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos):
                selection = 'rock'
                option = choose_random_option()
            elif paper_rect.collidepoint(event.pos):
                selection = 'paper'
            elif scissors_rect.collidepoint(event.pos):
                selection = 'scissors'
            elif quit_button.collidepoint(event.pos):
                running = False
    # Fill the screen with a color (optional)
    screen.fill((30, 30, 30))  # Black color
    screen.blit(rock_img, rock_rect)
    screen.blit(paper_img, paper_rect)
    screen.blit(scissors_img, scissors_rect)

    pygame.draw.rect(screen, (200, 0, 0), quit_button)  # Red button
    screen.blit(quit_text, quit_button.topleft)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
