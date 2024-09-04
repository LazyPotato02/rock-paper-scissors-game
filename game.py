import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.font.init()
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

image_map = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}
player_score = 0
computer_score = 0
def choose_random_option():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)


def determine_winner(player_choice, computer_choice):
    choices = ["rock", "paper", "scissors"]

    # Validate inputs
    if player_choice not in choices or computer_choice not in choices:
        return "Invalid choice. Must be 'Rock', 'Paper', or 'Scissors'.", 0, 0

    # Determine the winner
    if player_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!", 1, 0
    else:
        return "Computer wins!", 0, 1


def render_text(winner):
    text_color = (255, 255, 255)  # White color
    text_surface = font.render(winner, True, text_color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    return text_surface, text_rect
def render_score(player_score, computer_score):
    score_text = f"Player: {player_score}   Computer: {computer_score}"
    text_color = (255, 255, 255)  # White color
    score_surface = font.render(score_text, True, text_color)
    score_rect = score_surface.get_rect(center=(screen_width // 2, 50))
    return score_surface, score_rect

# Main loop
running = True
current_text_surface = None
current_text_rect = None
computer_image = None
computer_image_rect = None

while running:
    selection = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos):
                selection = 'rock'
            elif paper_rect.collidepoint(event.pos):
                selection = 'paper'
            elif scissors_rect.collidepoint(event.pos):
                selection = 'scissors'
            elif quit_button.collidepoint(event.pos):
                running = False
            else:
                continue
            # Get computer's choice and determine result
            option = choose_random_option()
            result, player_increment, computer_increment = determine_winner(selection, option)
            player_score += player_increment
            computer_score += computer_increment
            current_text_surface, current_text_rect = render_text(result)
            # Set computer image based on choice
            computer_image = image_map[option]
            computer_image_rect = computer_image.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    # Fill the screen with a color (optional)
    screen.fill((30, 30, 30))  # Black color
    screen.blit(rock_img, rock_rect)
    screen.blit(paper_img, paper_rect)
    screen.blit(scissors_img, scissors_rect)

    pygame.draw.rect(screen, (200, 0, 0), quit_button)  # Red button
    screen.blit(quit_text, quit_button.topleft)

    # Display the result text if available
    if current_text_surface and current_text_rect:
        screen.blit(current_text_surface, current_text_rect)

    if computer_image and computer_image_rect:
        screen.blit(computer_image, computer_image_rect)
    score_surface, score_rect = render_score(player_score, computer_score)
    screen.blit(score_surface, score_rect)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
