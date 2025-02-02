import pygame


def draw_rect():
    screen.fill("black")
    for el in arr:
        pygame.draw.rect(screen, "white", el, width=3)
    x2, y2 = event.pos
    w, h = abs(x1 - x2), abs(y1 - y2)
    x = x1 if x1 < x2 else x2
    y = y1 if y1 < y2 else y2
    pygame.draw.rect(screen, "white", (x, y, w, h), width=3)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill("black")
    running = True

    arr = []
    x1, y1 = None, None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                x2, y2 = event.pos
                w, h = abs(x1 - x2), abs(y1 - y2)
                x = x1 if x1 < x2 else x2
                y = y1 if y1 < y2 else y2
                arr.append((x, y, w, h))
                x1, y1 = None, None
            if event.type == pygame.MOUSEMOTION:
                if x1 and y1:
                    draw_rect()
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_LCTRL] and pygame.key.get_pressed()[pygame.K_z]:
                    if arr:
                        arr.pop()
                    screen.fill("black")
                    for el in arr:
                        pygame.draw.rect(screen, "white", el, width=3)
                    pygame.display.flip()

    pygame.quit()
