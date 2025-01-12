import pygame

import sys


def draw_rhomb(screen):
    for i in range(width // n):
        for j in range(height // n):
            x = n // 2 + n * j
            y = n // 2 + n * i
            pygame.draw.polygon(screen, "orange", [(x + n // 2, y),
                                                   (x, y - n // 2),
                                                   (x - n // 2, y),
                                                   (x, y + n // 2)])


if __name__ == "__main__":
    try:
        n = int(input())
        if n < 1:
            raise ValueError
    except ValueError:
        print("Неверный формат ввода!")
        sys.exit(0)
    pygame.init()

    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ромбики")

    screen.fill("yellow")

    draw_rhomb(screen)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()

