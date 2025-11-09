import pygame
from snake.game import SnakeGame

class PygameHandler:
    def __init__(self, width, height, cell_size=32):
        pygame.init()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width*cell_size, height*cell_size))
        pygame.display.set_caption("Snake TDD")
        self.clock = pygame.time.Clock()
        self.last_input = 'up'

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.last_input = 'up'
                elif event.key == pygame.K_s:
                    self.last_input = 'down'
                elif event.key == pygame.K_a:
                    self.last_input = 'left'
                elif event.key == pygame.K_d:
                    self.last_input = 'right'
        return None

    def draw(self, game):
        self.screen.fill((0,0,0))  # fundo preto

        # desenha fruta
        for fx, fy in game.fruits:
            pygame.draw.rect(self.screen, (255,0,0), (fx*self.cell_size, fy*self.cell_size, self.cell_size, self.cell_size))

        # desenha cobra
        for i, (x,y) in enumerate(game.snake):
            pygame.draw.rect(self.screen, (0,255,0), (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
        
        pygame.display.flip()
        self.clock.tick(10)
