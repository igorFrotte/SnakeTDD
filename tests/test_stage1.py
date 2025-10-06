import pytest
from snake.game import SnakeGame


@pytest.fixture
def game():
    return SnakeGame(width=10, height=10)


# --- Testes básicos do jogo ---

def test_initial_state(game):
    """O jogo deve iniciar com cobra de tamanho 2 e uma fruta dentro da área."""
    assert len(game.snake) == 2
    x, y = game.fruit
    assert 0 <= x < game.width
    assert 0 <= y < game.height


@pytest.mark.parametrize("direction", ["up", "down", "left", "right"])
def test_snake_moves_in_valid_directions(game, direction):
    """A cobra deve conseguir se mover em qualquer direção válida."""
    game.change_direction(direction)
    old_head = game.snake[0]
    game.step()  # faz um movimento
    new_head = game.snake[0]
    assert old_head != new_head


def test_snake_grows_after_eating(game):
    """A cobra deve crescer ao comer a fruta."""
    game.fruit = game.snake[0]  # força fruta na cabeça
    size_before = len(game.snake)
    game.step()
    assert len(game.snake) == size_before + 1


def test_snake_collision_with_itself(game):
    """O jogo deve detectar quando a cobra colide com o próprio corpo."""
    game.snake = [(5, 5), (5, 6), (6, 6), (6, 5), (5, 5)]
    assert game.check_collision() is True