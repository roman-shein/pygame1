import pygame


def moving(vx, vy):
    global x, y, new_x, new_y, v_x, v_y
    if vx or vy:
        x += vx
        y += vy
        v_x = vx if x != new_x else 0
        v_y = vy if y != new_y else 0
    else:
        new_x = new_y = 0


if __name__ == "__main__":
    pygame.init()

    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)

    FPS = 60
    x, y = width // 2, height // 2
    r = 20

    v_x = v_y = 0
    new_x = new_y = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill("black")
        pygame.draw.circle(screen, "red", (x, y), r)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not new_x and not new_y:
                    new_x, new_y = event.pos
                    if new_x < x:
                        v_x = -1
                    elif new_x > x:
                        v_x = 1
                    if new_y < y:
                        v_y = -1
                    elif new_y > y:
                        v_y = 1

        moving(v_x, v_y)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
