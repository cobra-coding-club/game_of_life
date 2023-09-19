import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of each grid location
WIDTH = 20
HEIGHT = 20

# Set the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.

class grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0 for x in range(columns)] for y in range(rows)]

    def __str__(self):
        return str(self.grid)

    def get(self, row, column):
        return self.grid[row][column]

    def set(self, row, column, value):
        self.grid[row][column] = value

    def get_neighbours(self, row, column):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if row + i < 0 or row + i >= self.rows:
                    continue
                if column + j < 0 or column + j >= self.columns:
                    continue
                neighbours.append(self.get(row + i, column + j))
        return neighbours

    def count_neighbours(self, row, column):
        return sum(self.get_neighbours(row, column))

    def next_state(self, row, column):
        neighbours = self.count_neighbours(row, column)
        if self.get(row, column) == 1:
            if neighbours < 2:
                return 0
            elif neighbours == 2 or neighbours == 3:
                return 1
            elif neighbours > 3:
                return 0
        else:
            if neighbours == 3:
                return 1
        return 0

    def next(self):
        new_grid = grid(self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                new_grid.set(row, column, self.next_state(row, column))
        return new_grid

# Initialize pygame
pygame.init()

gameGrid = grid(30, 30)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize first state cells
gameGrid.set(1, 2, 1)
gameGrid.set(2, 2, 1)
gameGrid.set(3, 2, 1)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # update the grid every 2 second
    if pygame.time.get_ticks() % 60 == 0:
        gameGrid = gameGrid.next()

    # Draw the grid
    for row in range(gameGrid.rows):
        for column in range(gameGrid.columns):
            color = WHITE
            if gameGrid.get(row, column) == 1:
                color = BLACK
            pygame.draw.rect(
                screen,
                color,
                [
                    (MARGIN + WIDTH) * column + MARGIN,
                    (MARGIN + HEIGHT) * row + MARGIN,
                    WIDTH,
                    HEIGHT,
                ],
            )
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
