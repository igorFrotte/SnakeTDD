# Snake TDD Game

Este é um projeto de implementação do clássico jogo **Snake**, desenvolvido seguindo os princípios de **Test Driven Development (TDD)**. O projeto também foi estruturado para, futuramente, permitir integração com algoritmos de Machine Learning que aprendam a jogar o jogo com base nas tentativas da cobra.

---

## 📝 Descrição

* A cobra cresce ao comer frutas.
* O jogo termina quando a cobra colide com o próprio corpo.
* A cobra pode atravessar as bordas da tela (wrap-around).
* Quando a cobra atinge tamanho 10, duas frutas aparecem simultaneamente; quando atinge tamanho 20, três frutas, e assim por diante.
* O projeto foi desenvolvido em etapas, usando TDD, garantindo testes unitários de cada funcionalidade.

---

## ⚙️ Bibliotecas necessárias

Para rodar o projeto, você precisará das seguintes bibliotecas Python:

* `keyboard` – captura do teclado (necessita root no Linux)

  ```bash
  pip install keyboard
  ```
* `pytest` – para rodar os testes

  ```bash
  pip install pytest
  ```

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

2. Rodar o jogo com permissões de root (necessário para `keyboard`):

```bash
sudo ./venv/bin/python3 run_game.py
```

3. Controles:

* **W** → mover para cima
* **S** → mover para baixo
* **A** → mover para esquerda
* **D** → mover para direita
* **ESC** → sair do jogo

4. O jogo atualiza a cada `game_speed` segundos (configurável no `io_handler`).

---

## 🧪 Rodando os testes

Para executar todos os testes unitários (Stages 1, 2 e 3):

```bash
pytest -v
```

> Certifique-se de estar no ambiente virtual com todas as dependências instaladas.

---

## 🔮 Futuro

* Integração com algoritmos de Machine Learning para treinar a cobra automaticamente.
* Ajustes na interface para melhor experiência visual e feedback.

---
