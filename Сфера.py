import pygame
import sys


def draw(screen):
    for i in range(n):
        pygame.draw.ellipse(screen, "white", (150 // n * i, 0, 300 - 150 // n * i * 2, 300), width=1)
        pygame.draw.ellipse(screen, "white", (0, 150 // n * i, 300, 300 - 150 // n * i * 2), width=1)


if __name__ == "__main__":
    try:
        n = int(input())
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Неверный формат ввода!")
        sys.exit(0)
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Сфера")

    screen.fill("black")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
