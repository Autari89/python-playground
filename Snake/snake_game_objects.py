import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen size
display_width = 800
display_height = 600

# Create the game window
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the snake
clock = pygame.time.Clock()

# Snake settings
single_block_dimension = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score = 0

class Food:
    def __init__(self):
        self.xPosition = round(random.randrange(
            0, display_width - single_block_dimension) / 10.0) * 10.0
        self.yPosition = round(random.randrange(
            0, display_height - single_block_dimension) / 10.0) * 10.0

    def UpdatePosition(self):
        self.xPosition = round(random.randrange(
            0, display_width - single_block_dimension) / 10.0) * 10.0
        self.yPosition = round(random.randrange(
            0, display_height - single_block_dimension) / 10.0) * 10.0


class Snake:
    def __init__(self, xHead, yHead):
        self.xHead = xHead
        self.yHead = yHead
        self.xVariation = 0
        self.yVariation = 0
        self.snakeLength = 1
        self.snakeBody = [[self.xHead, self.yHead]]

    def UpdateSnakeDirection(self, eventKey):
        if eventKey == pygame.K_LEFT:
            self.xVariation -= single_block_dimension
            self.yVariation = 0
        elif eventKey == pygame.K_RIGHT:
            self.xVariation += single_block_dimension
            self.yVariation = 0
        elif eventKey == pygame.K_UP:
            self.yVariation -= single_block_dimension
            self.xVariation = 0
        elif eventKey == pygame.K_DOWN:
            self.yVariation += single_block_dimension
            self.xVariation = 0

    def UpdateSnake(self):
        self.xHead += self.xVariation
        self.yHead += self.yVariation
        snakeHead = [self.xHead, self.yHead]
        self.snakeBody.append(snakeHead)
        if len(self.snakeBody) > self.snakeLength:
            del self.snakeBody[0]

    def HitWalls(self):
        return self.xHead >= display_width or self.xHead <= 0 or self.yHead >= display_height or self.yHead <= 0

    def HitItself(self):
        snakeHead = [self.xHead, self.yHead]
        for singleSnakeBlock in self.snakeBody[:-1]:
            if singleSnakeBlock == snakeHead:
                return True
        return False

    def HitFood(self, food):
        return self.xHead == food.xPosition and self.yHead == food.yPosition

    def IncreaseLength(self):
        self.snakeLength += 1


def DisplayScore(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])


def DrawSnake(snakeToDraw):
    for block in snakeToDraw.snakeBody:
        pygame.draw.rect(display, green, [
                         block[0], block[1], single_block_dimension, single_block_dimension])


def gameLoop():
    game_over = False
    game_close = False

    food = Food()
    snake = Snake(display_width/2, display_height/2)

    while not game_over:
        while game_close:
            display.fill(black)
            message = font_style.render(
                "Game Over! Press Q to quit or C to Play Again", True, red)
            display.blit(message, [display_width / 6, display_height / 3])
            DisplayScore(snake.snakeLength)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                snake.UpdateSnakeDirection(event.key)
        
        snake.UpdateSnake()
        
        if (snake.HitWalls() or snake.HitItself()):
            game_close = True
            continue

        if (snake.HitFood(food)):
            food.UpdatePosition()
            snake.IncreaseLength()

        display.fill(black)
        pygame.draw.rect(display, blue, [
                         food.xPosition, food.yPosition, single_block_dimension, single_block_dimension])
        DrawSnake(snake)
        DisplayScore(snake.snakeLength - 1)
        pygame.display.update()
        clock.tick(snake_speed)


if __name__ == "__main__":
    gameLoop()
