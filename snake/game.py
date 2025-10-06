
class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = []
        self.fruit = None
        self.reward = 0
        self.done = False

    def change_direction(self, direction):
        pass

    def step(self):
        """Executa uma jogada (ação) e retorna o estado observável."""
        pass

    def check_collision(self):
        pass