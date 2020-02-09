import pygame, time, sys
from pygame.locals import *

# pygame setup stuff
pygame.init()
WINWIDTH = 640
WINHEIGHT = 480
windowSurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
pygame.display.set_caption('Sierpinski Triangles')


# define a bunch of constants:
DELAY = 1.5 # seconds between showing the next level
MAXLEVEL = 8 # the largest number of levels for the animation to show

#                 R    G    B
RED           = (255,   0,   0)
WHITE         = (255, 255, 255)
DARKTURQUOISE = (  3,  54,  73)
TURQUOISE     = (103, 154, 173)
GREEN         = (  0, 204,   0)
PURPLE        = (238, 130, 238)


WINDOW_BG = TURQUOISE
TRIANGLE_FG = PURPLE
TRIANGLE_BG = DARKTURQUOISE

SAVEIMAGES = False
if SAVEIMAGES:
    DELAY = 0.0


def drawSierpinkski(surf, rect, fgcolor, bgcolor, level=6):
    # Draws sierpinkski triangles inside the given rect object on the surf surface.

    if level == 0: # base triangle
        return

    # calculate the point one quarter and three quarters in the rect
    quarterWidth = (rect.width / 4) + rect.left
    threeQuarterWidth = (rect.width / 4 * 3) + rect.left

    # draw the outer triangle:
    pygame.draw.polygon(surf, fgcolor, ((rect.centerx, rect.top), (rect.left, rect.bottom), (rect.right, rect.bottom)))
    # draw the upside down inner triangle:
    pygame.draw.polygon(surf, bgcolor, ((quarterWidth, rect.centery), (rect.centerx, rect.bottom), (threeQuarterWidth, rect.centery)))

    # calculate the rectangular outlines
    topRect   = pygame.Rect(quarterWidth, rect.top,     (rect.width / 2), (rect.height / 2))
    leftRect  = pygame.Rect(rect.left,    rect.centery, (rect.width / 2), (rect.height / 2))
    rightRect = pygame.Rect(rect.centerx, rect.centery, (rect.width / 2), (rect.height / 2))

    # level tends to 0
    drawSierpinkski(surf, topRect, fgcolor, bgcolor, level-1)
    drawSierpinkski(surf, leftRect, fgcolor, bgcolor, level-1)
    drawSierpinkski(surf, rightRect, fgcolor, bgcolor, level-1)


def main():
    levelCounter = 0
    startTime = time.time() - DELAY
    saveCounter = 0
    saveTimestamp = int(time.time())

    while True:
        if time.time() > startTime + DELAY:
            # after DELAY seconds have passed, increment the level and draw it
            levelCounter += 1
            if levelCounter >= MAXLEVEL:
                # once we reach level 8, reset it back to 1.
                levelCounter = 1
                SAVEIMAGES = False

            windowSurface.fill(WINDOW_BG)
            # draw the sierpinkski triangles
            drawSierpinkski(windowSurface, pygame.Rect(0, 0, WINWIDTH, WINHEIGHT), TRIANGLE_FG, TRIANGLE_BG, levelCounter)

            startTime = time.time() # reset the timer
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()