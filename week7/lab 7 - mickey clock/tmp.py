import pygame as pg


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pg.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


def main():
    path = r"C:/pp2/week7/lab 7 - mickey clock/" 
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    gray = pg.Color('gray15')

    image = pg.image.load(path + "arrow_b.png")
    orig_image = image
    rect = image.get_rect(center=(320, 240))
    angle = 0

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        angle += 2
        image, rect = rotate(orig_image, rect, angle)

        screen.fill(gray)
        screen.blit(image, rect)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()