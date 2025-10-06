import time
from snake.game import SnakeGame
from snake_screen import io_handler

def main():
    game = SnakeGame(width=10, height=10)
    io = io_handler((10,10), 0.3)
    io.record_inputs()  # só usado no jogo real

    try:
        while True:
            last = io.last_input
            if last == "w":
                game.change_direction("up")
            elif last == "s":
                game.change_direction("down")
            elif last == "a":
                game.change_direction("left")
            elif last == "d":
                game.change_direction("right")
            elif last == "end":
                break

            game.step()

            io.matrix = [[0]*io.x_size for _ in range(io.y_size)]
            for x, y in game.snake:
                io.matrix[y][x] = 1
            hx, hy = game.snake[0]
            io.matrix[hy][hx] = 2
            if game.fruits:
                for fx, fy in game.fruits:
                    io.matrix[fy][fx] = 3

            io.display()

            if game.check_collision():
                print("Game Over! Você bateu na própria cobra.")
                break

            time.sleep(io.game_speed)

    except KeyboardInterrupt:
        print("\nJogo interrompido.")

if __name__ == "__main__":
    main()
