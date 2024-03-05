import pygame
import os

WIDTH, HEIGHT = 1000, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Adventure 2.0")
WHITE = (255, 255, 255)
Home_Image = pygame.image.load(os.path.join('Image.jpg'))
Home = pygame.transform.scale(Home_Image, (1000, 450))


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(Home, (10, 5))
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    # pygame.quit()


if __name__ == "__main__":
    draw_window()
    main()
