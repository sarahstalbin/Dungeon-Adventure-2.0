import sys

import pygame
import os

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1000, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Adventure 2.0")
WHITE = (255, 255, 255)
Home_Image = pygame.image.load(os.path.join('Image.jpg'))
Home = pygame.transform.scale(Home_Image, (1000, 450))
font = pygame.font.Font(None, 36)


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(Home, (10, 5))
    pygame.display.update()


def main():
    run = True
    start_game = False
    end_game = False
    # font = pygame.font.Font(None, 36)
    text = font.render(" Start Game", True, (0, 0, 0))
    end = font.render("End Game", True, (0,0,0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
    end_rect = end.get_rect(center=(WIDTH // 2, HEIGHT // 1.4))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    end_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    if text_rect.collidepoint(event.pos):
                        start_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    if end_rect.collidepoint(event.pos):
                        end_game = True
        # WIN.fill((0, 0, 0))
        WIN.blit(text, text_rect)
        WIN.blit(end, end_rect)
        pygame.display.flip()
        if start_game:
            # Perform actions to start the game here
            print("Game is starting!")
            run = False  # Exit the loop to start the game
        if end_game:
            # Perform actions to start the game here
            print("Game is ending!")
            run = False  # Exit the loop to start the game

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    draw_window()
    main()
