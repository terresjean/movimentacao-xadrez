# Movimentação de Peças de Xadrez

Este projeto apresenta uma implementação simples, didática e funcional das **movimentações básicas das principais peças de xadrez**, desenvolvido em Python. Ele foi criado para servir como atividade prática no curso de **Análise e Desenvolvimento de Sistemas (Estácio)** ou como exemplo introdutório para quem está aprendendo Orientação a Objetos.

---

## 🎯 Objetivo do Projeto

O objetivo é demonstrar:

* Uso de **classes e herança** em Python.
* Estruturação de um código simples e organizado.
* Lógica de movimentação das peças no tabuleiro.
* Execução de testes básicos de movimentação.

---

## 📌 Peças Implementadas

O projeto possui classes para as seguintes peças:

* **Torre** – movimentos horizontais e verticais.
* **Bispo** – movimentos diagonais.
* **Cavalo** – movimentos em "L".
* **Rei** – um passo em qualquer direção.
* **Rainha** – combinação de Torre + Bispo.
* **Peão** – movimento simples para frente.

Cada peça possui o método:

```
movimentos_possiveis(posicao)
```

Retorna todas as casas possíveis a partir da posição informada (ex.: `(4, 4)`).

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe ou clone este repositório.
3. Execute o arquivo principal:

```
python main.py
```

O programa exibirá no terminal os movimentos possíveis do Cavalo na posição `(4, 4)`.

---

## 📂 Estrutura do Projeto

```
movimentacao-xadrez/
│
├── main.py        # Código principal do projeto
└── README.md      # Descrição do projeto
```

---

## 📘 Exemplo de Saída

```
Movimentos possíveis do Cavalo:
[(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
```

---


