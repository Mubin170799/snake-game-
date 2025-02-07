import pygame
import random
from enum import Enum
from collections import namedtuple

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define game constants
BLOCK_SIZE = 20
SPEED = 10

class Direction(Enum):
    # for moving right (value: 1)
    RIGHT = 1
    # for moving left (value: 2) 
    LEFT = 2
    # for moving up (value: 3)
    UP = 3
    # Direction for moving down (value: 4)
    DOWN = 4

Point = namedtuple('Point', 'x, y')

class SnakeGame:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')

        # Initialize the clock for controlling the frame rate
        
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.width//2, self.height//2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2*BLOCK_SIZE), self.head.y)
        ]
        self.score = 0
        self.food = self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food = Point(x, y)
        if food in self.snake:
            return self._place_food()
        return food

    def play_step(self):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        # Move snake
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # Check game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # Check food collision
        if self.head == self.food:
            self.score += 1
            self.food = self._place_food()
        else:
            self.snake.pop()

        # Update UI
        self._update_ui()
        self.clock.tick(SPEED)

        return game_over, self.score

    def _is_collision(self):
        # Check if hit boundary
        if (self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or
            self.head.y > self.height - BLOCK_SIZE or self.head.y < 0):
            return True
        # Check if hit self
        if self.head in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = Point(x, y)

def main():
    game = SnakeGame()
    while True:
        game_over, score = game.play_step()
        if game_over:
            break
    pygame.quit()

if __name__ == "__main__":
    main() 