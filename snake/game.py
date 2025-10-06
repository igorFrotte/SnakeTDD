import random

class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

        # Inicializa a cobra com tamanho 2
        self.snake = [(width // 2, height // 2), (width // 2, height // 2 + 1)]
        self.direction = "up"

        # Coloca a primeira fruta
        self.place_fruit()

    def place_fruit(self):
        empty_cells = [(x, y) for x in range(self.width)
                       for y in range(self.height)
                       if (x, y) not in self.snake]
        self.fruit = random.choice(empty_cells) if empty_cells else None

    def change_direction(self, new_dir):
        allowed = {"up", "down", "left", "right"}
        if new_dir in allowed:
            # Evita mover na direção oposta
            opposite = {"up":"down", "down":"up", "left":"right", "right":"left"}
            if len(self.snake) > 1 and new_dir == opposite[self.direction]:
                return
            self.direction = new_dir

    def step(self):
        if not self.snake:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "up":
            head_y = (head_y - 1) % self.height
        elif self.direction == "down":
            head_y = (head_y + 1) % self.height
        elif self.direction == "left":
            head_x = (head_x - 1) % self.width
        elif self.direction == "right":
            head_x = (head_x + 1) % self.width

        new_head = (head_x, head_y)

        # cresce se comer fruta ou se a fruta estiver na posição da cabeça 
        if new_head == self.fruit or self.snake[0] == self.fruit:
            self.snake = [new_head] + self.snake  # cresce
            self.place_fruit()
        else:
            self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        if not self.snake:
            return False
        return self.snake[0] in self.snake[1:]
