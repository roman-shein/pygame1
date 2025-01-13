import pygame

WIDTH, HEIGHT = 29, 14


def draw_blocks(screen):
    for i in range(height // HEIGHT + 1):
        for j in range(width // WIDTH + 1):
            if i % 2 == 0:
                pygame.draw.rect(screen, "red", [WIDTH * j + 3 * j, HEIGHT * i + 3 * i, WIDTH, HEIGHT])
            else:
                pygame.draw.rect(screen, "red", [WIDTH * j + 3 * j - 15, HEIGHT * i + 3 * i, WIDTH, HEIGHT])


if __name__ == "__main__":
    pygame.init()

    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ромбики")

    screen.fill("white")

    draw_blocks(screen)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
