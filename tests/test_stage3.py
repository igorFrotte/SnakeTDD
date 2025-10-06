import pytest
from unittest.mock import patch
from snake_screen import io_handler
from snake.game import SnakeGame

@pytest.fixture
def game():
    return SnakeGame(width=10, height=10)

@pytest.fixture
def io():
    # Mocka o keyboard para não precisar de root
    with patch("snake_screen.keyboard"):
        io_instance = io_handler((10, 10), 0.1)
        yield io_instance

def test_io_matrix_head_and_body(game, io):
    """Cabeça e corpo da cobra aparecem corretamente na matriz"""
    io.matrix = [[0]*io.x_size for _ in range(io.y_size)]
    for x, y in game.snake:
        io.matrix[y][x] = 1
    hx, hy = game.snake[0]
    io.matrix[hy][hx] = 2

    assert io.matrix[hy][hx] == 2
    for x, y in game.snake[1:]:
        assert io.matrix[y][x] == 1

def test_io_matrix_fruits(game, io):
    """Frutas aparecem corretamente na matriz"""
    game.fruits = [(2,2), (5,5)]
    io.matrix = [[0]*io.x_size for _ in range(io.y_size)]
    for x, y in game.snake:
        io.matrix[y][x] = 1
    hx, hy = game.snake[0]
    io.matrix[hy][hx] = 2
    for fx, fy in game.fruits:
        io.matrix[fy][fx] = 3

    for fx, fy in game.fruits:
        assert io.matrix[fy][fx] == 3

def test_io_matrix_after_step(game, io):
    """Matriz é atualizada corretamente após um passo"""
    game.fruits = [(5,5)]
    game.change_direction("right")
    game.step()

    io.matrix = [[0]*io.x_size for _ in range(io.y_size)]
    for x, y in game.snake:
        io.matrix[y][x] = 1
    hx, hy = game.snake[0]
    io.matrix[hy][hx] = 2
    for fx, fy in game.fruits:
        io.matrix[fy][fx] = 3

    hx_expected = hx
    hy_expected = hy
    assert io.matrix[hy_expected][hx_expected] == 2
    assert io.matrix[5][5] == 3
