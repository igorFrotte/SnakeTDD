import pytest
from snake.game import SnakeGame

@pytest.fixture
def game():
    return SnakeGame(width=10, height=10)

def test_initial_number_of_fruits(game):
    """No início, deve ter apenas 1 fruta"""
    assert len(game.fruits) == 1

def test_two_fruits_after_size_10(game):
    """Quando a cobra atingir tamanho 10, devem aparecer 2 frutas"""
    # força o crescimento da cobra
    game.snake = [(0,0)] * 10
    game.update_fruits()  # método que vamos criar
    assert len(game.fruits) == 2

def test_three_fruits_after_size_20(game):
    """Quando a cobra atingir tamanho 20, devem aparecer 3 frutas"""
    game.snake = [(0,0)] * 20
    game.update_fruits()
    assert len(game.fruits) == 3
