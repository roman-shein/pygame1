import pygame

from math import cos, radians, tan


def rotation(screen):
    cur_d = a / FPS
    for d1, d2 in arr:
        cur_d += d1
        x1 = -70 * cos(radians(cur_d))
        y1 = x1 * tan(radians(cur_d))

        cur_d += d2
        x2 = -70 * cos(radians(cur_d))
        y2 = x2 * tan(radians(cur_d))

        pygame.draw.polygon(screen, "white", ((x1 + half_width, y1 + half_height),
                                              (x2 + half_width, y2 + half_height),
                                              (half_width, half_height)))

    pygame.draw.circle(screen, "white", (width // 2, height // 2), 10)


if __name__ == "__main__":
    pygame.init()

    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    half_width, half_height = width // 2, height // 2
    v = 0
    a = 0
    FPS = 50

    clock = pygame.time.Clock()

    running = True

    arr = [(75, 30), (90, 30), (90, 30)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    v += 50
                if event.button == pygame.BUTTON_RIGHT:
                    v -= 50
        a += v
        screen.fill("black")
        rotation(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
