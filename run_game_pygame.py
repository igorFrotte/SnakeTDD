from snake.game import SnakeGame
from snake.pygame_handler import PygameHandler

def main():
    game = SnakeGame(10, 10)
    io = PygameHandler(10, 10, cell_size=32, fps=10, asset_path="assets")

    running = True
    while running:
        action = io.get_input()
        if action == "quit":
            break
        game.change_direction(action)
        game.step()
        io.draw(game)
        if game.check_collision():
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
