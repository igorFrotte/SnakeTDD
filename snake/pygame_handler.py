import pygame
from pygame.locals import *
import os

class PygameHandler:
    def __init__(self, game_width, game_height, cell_size=32, fps=10, asset_path="assets"):
        """
        Inicializa o Pygame e carrega os assets.
        game_width, game_height: tamanho da matriz do jogo
        cell_size: tamanho de cada célula em pixels
        fps: frames por segundo
        asset_path: pasta com os sprites
        """
        pygame.init()
        self.game_width = game_width
        self.game_height = game_height
        self.cell_size = cell_size
        self.fps = fps
        self.screen = pygame.display.set_mode((game_width*cell_size, game_height*cell_size))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # Carregar sprites
        self.assets = {}
        for name in ["head_up", "head_down", "head_left", "head_right",
                     "tail_up", "tail_down", "tail_left", "tail_right",
                     "body_vertical", "body_horizontal",
                     "body_curve_ul", "body_curve_ur", "body_curve_dl", "body_curve_dr",
                     "fruit"]:
            self.assets[name] = pygame.image.load(os.path.join(asset_path, f"{name}.png")).convert_alpha()

        self.last_input = "up"

    def get_input(self):
        """
        Captura inputs do jogador para mudar a direção.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    self.last_input = "up"
                elif event.key == K_s:
                    self.last_input = "down"
                elif event.key == K_a:
                    self.last_input = "left"
                elif event.key == K_d:
                    self.last_input = "right"
                elif event.key == K_ESCAPE:
                    return "quit"
        return self.last_input

    def draw(self, game):
        """
        Desenha a tela inteira do jogo.
        game: instância de SnakeGame
        """
        self.screen.fill((0, 0, 0))  # fundo preto

        snake = game.snake
        fruits = game.fruits

        # Desenha frutas
        for fx, fy in fruits:
            self.screen.blit(self.assets["fruit"], (fx*self.cell_size, fy*self.cell_size))

        # Desenha corpo da cobra
        for i, (x, y) in enumerate(snake):
            if i == 0:
                # cabeça
                if len(snake) > 1:
                    nx, ny = snake[1]
                    if nx < x:
                        self.screen.blit(self.assets["head_right"], (x*self.cell_size, y*self.cell_size))
                    elif nx > x:
                        self.screen.blit(self.assets["head_left"], (x*self.cell_size, y*self.cell_size))
                    elif ny < y:
                        self.screen.blit(self.assets["head_down"], (x*self.cell_size, y*self.cell_size))
                    elif ny > y:
                        self.screen.blit(self.assets["head_up"], (x*self.cell_size, y*self.cell_size))
                else:
                    self.screen.blit(self.assets["head_up"], (x*self.cell_size, y*self.cell_size))
            elif i == len(snake)-1:
                # cauda
                px, py = snake[i-1]
                if px < x:
                    self.screen.blit(self.assets["tail_right"], (x*self.cell_size, y*self.cell_size))
                elif px > x:
                    self.screen.blit(self.assets["tail_left"], (x*self.cell_size, y*self.cell_size))
                elif py < y:
                    self.screen.blit(self.assets["tail_down"], (x*self.cell_size, y*self.cell_size))
                elif py > y:
                    self.screen.blit(self.assets["tail_up"], (x*self.cell_size, y*self.cell_size))
            else:
                # corpo
                px, py = snake[i-1]
                nx, ny = snake[i+1]
                if px == nx:
                    self.screen.blit(self.assets["body_vertical"], (x*self.cell_size, y*self.cell_size))
                elif py == ny:
                    self.screen.blit(self.assets["body_horizontal"], (x*self.cell_size, y*self.cell_size))
                else:
                    # curva
                    if (px < x and ny < y) or (nx < x and py < y):
                        self.screen.blit(self.assets["body_curve_ul"], (x*self.cell_size, y*self.cell_size))
                    elif (px > x and ny < y) or (nx > x and py < y):
                        self.screen.blit(self.assets["body_curve_ur"], (x*self.cell_size, y*self.cell_size))
                    elif (px < x and ny > y) or (nx < x and py > y):
                        self.screen.blit(self.assets["body_curve_dl"], (x*self.cell_size, y*self.cell_size))
                    elif (px > x and ny > y) or (nx > x and py > y):
                        self.screen.blit(self.assets["body_curve_dr"], (x*self.cell_size, y*self.cell_size))

        pygame.display.update()
        self.clock.tick(self.fps)
