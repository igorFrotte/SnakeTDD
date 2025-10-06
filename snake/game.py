import random

class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2), (width//2, height//2 + 1)]
        self.direction = "up"
        self.fruits = []
        self.update_fruits()

    def update_fruits(self):
        """Define quantas frutas devem existir com base no tamanho da cobra"""
        num_fruits = 1 + (len(self.snake) // 10)
        # mantém frutas existentes, adiciona novas se necessário
        while len(self.fruits) < num_fruits:
            self.place_new_fruit()

    def place_new_fruit(self):
        empty_cells = [(x, y) for x in range(self.width)
                    for y in range(self.height)
                    if (x, y) not in self.snake and (x, y) not in self.fruits]
        if empty_cells:
            self.fruits.append(random.choice(empty_cells))


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

        # verifica se comeu alguma fruta
        if new_head in self.fruits:
            self.snake = [new_head] + self.snake
            self.fruits.remove(new_head)
            self.update_fruits()
        else:
            self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        if not self.snake:
            return False
        return self.snake[0] in self.snake[1:]
