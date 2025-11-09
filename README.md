# Snake TDD Game (com Pygame)

Este é um projeto de implementação do clássico jogo **Snake**, desenvolvido seguindo os princípios de **Test Driven Development (TDD)**. O projeto também foi estruturado para permitir futuras integrações com algoritmos de Machine Learning que aprendam a jogar o jogo com base nas tentativas da cobra.

---

## 📝 Descrição

* A cobra cresce ao comer frutas.
* O jogo termina quando a cobra colide com o próprio corpo.
* A cobra pode atravessar as bordas da tela (wrap-around).
* Quando a cobra atinge tamanho 10, duas frutas aparecem simultaneamente; quando atinge tamanho 20, três frutas, e assim por diante.
* O projeto foi desenvolvido em etapas, usando TDD, garantindo testes unitários de cada funcionalidade.
* A partir da Stage 4, o jogo utiliza **Pygame** para exibição e captura de inputs, substituindo o antigo `keyboard`.

---

## ⚙️ Bibliotecas necessárias

Para rodar o projeto, você precisará das seguintes bibliotecas Python:

* `pygame` – motor gráfico e captura de inputs

```bash
pip install pygame
```

* `pytest` – para rodar os testes

```bash
pip install pytest
```

> Não é mais necessário usar `keyboard` nem permissões de root no Linux.

---

## ▶️ Como jogar

1. Clone o repositório e crie um ambiente virtual:

```bash
git clone <url-do-repositorio>
cd TDD---Exercicio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Rodar o jogo:

```bash
python3 run_game.py
```

3. Controles:

* **W** → mover para cima
* **S** → mover para baixo
* **A** → mover para esquerda
* **D** → mover para direita
* **ESC** → sair do jogo

4. Configuração visual:

* A janela é definida pelo **tamanho da matriz do jogo** (`game_width` x `game_height`) e pelo **tamanho das células** (`cell_size`) no `PygameHandler`.
* Exemplo de inicialização com janela maior:

```python
game = SnakeGame(width=20, height=20)
io_handler = PygameHandler(game_width=20, game_height=20, cell_size=40)
```

---

## 🧪 Rodando os testes

Para executar todos os testes unitários (Stages 1, 2, 3 e 4):

```bash
pytest -v
```

> Certifique-se de estar no ambiente virtual com todas as dependências instaladas.

---

## 🔮 Futuro

* Integração com algoritmos de Machine Learning para treinar a cobra automaticamente.
* Ajustes na interface para melhor experiência visual e feedback.
