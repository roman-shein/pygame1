import pygame


def read_file():
    with open("points.txt", 'r', encoding="utf8") as f:
        for el in f.read().split(", "):
            new_el = list(map(float, el.rstrip(')').lstrip('(').replace(',', '.').split(';')))
            arr.append(tuple(new_el))


def draw_polygon():
    new_arr = update_arr()
    pygame.draw.polygon(screen, "white", new_arr, width=1)


def update_arr():
    new_arr = []
    for x, y in arr:
        new_arr.append((x * k + dx, -y * k + dy))

    return new_arr


if __name__ == "__main__":
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)

    dx, dy = width // 2, height // 2
    arr = []
    read_file()

    k = 10

    running = True
    screen.fill("black")
    draw_polygon()
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                k += event.y
                k = k if k > 0 else 1
                screen.fill("black")
                draw_polygon()
                pygame.display.flip()

    pygame.quit()
