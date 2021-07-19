# import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (178, 102, 255)
cellWidth = 50
cellHeight = 50
MARGIN = 5


class DrawPuzzle:

    def __init__(self, n, stages):
        self.size = n
        self.stages = stages
        self.matrix = stages[0]
        self.oneImg = pygame.image.load('icons/one.png')
        self.zeroImg = pygame.image.load('icons/zero.png')

    def calcXY(self, x, y):
        xy = [x * (cellWidth + MARGIN) + ((cellWidth - 24) / 2), y * (cellHeight + MARGIN) + ((cellHeight - 24) / 2)]
        return xy

    def draw(self):
        i = 0
        pygame.init()
        WINDOW_SIZE = [self.size * (cellWidth + MARGIN) + MARGIN, self.size * (cellHeight + MARGIN) + MARGIN]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Binary Puzzle")
        # pygame.display.toggle_fullscreen()
        done = False
        clock = pygame.time.Clock()

        while not done:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            for row in range(self.size):
                for column in range(self.size):
                    color = WHITE
                    if self.matrix[row][column] == '-':
                        color = GREEN
                    pygame.draw.rect(screen, color,
                                     [(MARGIN + cellWidth) * column + MARGIN,
                                      (MARGIN + cellHeight) * row + MARGIN,
                                      cellWidth,
                                      cellHeight])
                    xy = self.calcXY(column, row)
                    if self.matrix[row][column] == 0:
                        screen.blit(self.zeroImg, (xy[0], xy[1]))
                    elif self.matrix[row][column] == 1:
                        screen.blit(self.oneImg, (xy[0], xy[1]))
            i += 1
            if i < len(self.stages):
                self.matrix = self.stages[i]

            pygame.time.wait(1000)
            pygame.display.update()
        pygame.quit()