import pygame


def print_num(screen):
    font = pygame.font.Font(None, 100)
    text = font.render(str(c), True, (255, 0, 0))

    text_w = text.get_width()
    text_h = text.get_height()

    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2

    screen.blit(text, (text_x, text_y))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Я слежу за тобой!")

    screen.fill("black")

    running = True
    c = 1

    print_num(screen)

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWMINIMIZED:
                c += 1
        screen.fill("black")
        print_num(screen)
        pygame.display.flip()

    pygame.quit()
