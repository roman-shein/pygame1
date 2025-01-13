import sys
import pygame


def draw_cube(screen):
    color = pygame.Color("white")
    color.hsva = (hue, 100, 75)
    pygame.draw.rect(screen, color, [width // 2 - w // 2, height // 2 - w // 2, w, w])

    color.hsva = (hue, 100, 100)
    pygame.draw.polygon(screen, color, [(width // 2 - w // 2, height // 2 - w // 2),
                                        (width // 2 + w // 2, height // 2 - w // 2),
                                        (width // 2 + w, height // 2 - w),
                                        (width // 2, height // 2 - w)])

    color.hsva = (hue, 100, 50)
    pygame.draw.polygon(screen, color, [(width // 2 + w // 2, height // 2 + w // 2),
                                        (width // 2 + w // 2, height // 2 - w // 2),
                                        (width // 2 + w, height // 2 - w),
                                        (width // 2 + w, height // 2)])


if __name__ == "__main__":
    try:
        w, hue = map(int, input().split())
        if w % 4 != 0 or w > 100 or not (0 <= hue <= 360):
            raise ValueError
    except ValueError:
        print("Неверный формат ввода!")
        sys.exit(0)
    pygame.init()

    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Куб")

    screen.fill("black")

    draw_cube(screen)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
