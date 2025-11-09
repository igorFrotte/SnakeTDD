import pytest
from unittest.mock import patch, MagicMock
from snake.game import SnakeGame
from snake.pygame_handler import PygameHandler

@pytest.fixture
def game():
    return SnakeGame(width=10, height=10)

@pytest.fixture
def pygame_io():
    """Instância do PygameHandler mockando tela e assets"""
    # Inicializa pygame
    import pygame
    pygame.init()

    # Cria handler com a assinatura correta
    io = PygameHandler(game_width=10, game_height=10, cell_size=20)

    # Mocka tela e assets para não depender de arquivos ou da tela real
    io.screen = MagicMock()
    for key in io.assets:
        io.assets[key] = MagicMock()

    yield io

def test_draw_called_for_snake_and_fruit(game, pygame_io):
    """Testa se draw chama blit para cobra e frutas"""
    game.snake = [(5,5), (5,6)]
    game.fruits = [(2,2)]

    # Mock display update
    pygame_io.draw(game)
    assert pygame_io.screen.blit.called
    # Verifica se todas as frutas e cabeça/corpo/cauda chamaram blit
    calls = pygame_io.screen.blit.call_args_list
    assert len(calls) >= len(game.snake) + len(game.fruits)

def test_get_input_updates_last_input(pygame_io):
    """Testa se get_input atualiza last_input"""
    import pygame
    event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_w})
    with patch("pygame.event.get", return_value=[event]):
        result = pygame_io.get_input()
    assert result == "up"
    assert pygame_io.last_input == "up"

def test_game_step_with_io(game, pygame_io):
    """Testa integração básica: step do jogo e draw"""
    game.snake = [(5,5), (5,6)]
    game.change_direction("up")

    # Mock display update
    pygame_io.draw(game)
    assert pygame_io.screen.blit.called
