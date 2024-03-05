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
button_width, button_height = 200, 40
easy_button = pygame.Rect(WIDTH // 2 - button_width // 2, 200, button_width, button_height)
medium_button = pygame.Rect(WIDTH // 2 - button_width // 2, 250, button_width, button_height)
hard_button = pygame.Rect(WIDTH // 2 - button_width // 2, 300, button_width, button_height)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(Home, (10, 5))
    pygame.draw.rect(WIN, (0, 0, 0), (WIDTH - 150, 10, 140, 40))
    menu_text = font.render("Menu", True, WHITE)
    WIN.blit(menu_text, (WIDTH - 75 - menu_text.get_width() // 2, 30 - menu_text.get_height() // 2))
    pygame.display.update()

def display_menu(menu):
    WIN.fill(WHITE)
    WIN.blit(Home, (10, 5))
    for i, line in enumerate(menu):
        text_surface = font.render(line, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 1.2, 50 + i * 30))
        WIN.blit(text_surface, text_rect)
    pygame.display.update()

def draw_difficulty_buttons():



    pygame.draw.rect(WIN, (0, 0, 0), easy_button)
    pygame.draw.rect(WIN, (0, 0, 0), medium_button)
    pygame.draw.rect(WIN, (0, 0, 0), hard_button)

    easy_text = font.render("Easy", True, WHITE)
    medium_text = font.render("Medium", True, WHITE)
    hard_text = font.render("Hard", True, WHITE)

    WIN.blit(easy_text, (WIDTH // 2 - easy_text.get_width() // 2, 200 + button_height // 2- easy_text.get_height() // 2))
    WIN.blit(medium_text, (WIDTH // 2 - medium_text.get_width() // 2, 250 + button_height // 2 - medium_text.get_height() // 2))
    WIN.blit(hard_text, (WIDTH // 2 - hard_text.get_width() // 2, 300 + button_height // 2 - hard_text.get_height() // 2))

    pygame.display.update()

def main():
    menu = [
        "Action Menu: m",
        "Go Up: w",
        "Go Down: s",
        "Go Left: a",
        "Go Right: d",
        "Use Health Potion: h",
        "Use Vision: v",
        "View current status: stats",
        "Quit Game: q"
    ]

    run = True
    start_game = False
    end_game = False
    difficulty_selected = False

    text = font.render("Start Game", True, (0, 0, 0))
    end = font.render("End Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
    end_rect = end.get_rect(center=(WIDTH // 2, HEIGHT // 1.4))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if text_rect.collidepoint(event.pos):
                        start_game = True
                    elif end_rect.collidepoint(event.pos):
                        end_game = True
                    elif WIDTH - 150 <= event.pos[0] <= WIDTH - 10 and 10 <= event.pos[1] <= 50:
                        display_menu(menu)

        WIN.blit(text, text_rect)
        WIN.blit(end, end_rect)
        pygame.display.flip()

        if start_game:
            draw_difficulty_buttons()
            while not difficulty_selected:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        difficulty_selected = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if easy_button.collidepoint(event.pos):
                                print("Easy difficulty selected!")
                                difficulty_selected = True
                            elif medium_button.collidepoint(event.pos):
                                print("Medium difficulty selected!")
                                difficulty_selected = True
                            elif hard_button.collidepoint(event.pos):
                                print("Hard difficulty selected!")
                                difficulty_selected = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    draw_window()
    main()
