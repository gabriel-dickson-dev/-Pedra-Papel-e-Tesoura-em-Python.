# -Pedra-Papel-e-Tesoura-em-Python.
Projeto desenvolvido em Python que simula o jogo Jokenpô (Pedra, Papel e Tesoura) entre o jogador e o computador.  O programa utiliza a biblioteca random para gerar a escolha do computador e estruturas condicionais para determinar o vencedor, empate ou derrota.
---
***O código faz uso de vários recursos nativos do Python para garantir que o jogo funcione de forma simples e sem erros de digitação:***

-import random: Importa a biblioteca nativa do Python responsável por gerar escolhas aleatórias.

-random.choice(): Função da biblioteca random usada para o computador escolher aleatoriamente um elemento da lista ["pedra", "papel", "tesoura"].

-.lower(): Converte o texto digitado pelo usuário para letras minúsculas. Assim, se você digitar "PEDRA" ou "Papel", o código entenderá normalmente.

-.strip(): Remove espaços em branco extras do início e do fim do texto digitado. Se o usuário digitar " pedra ", o método transforma em "pedra".

-input(): Captura o texto que o jogador digita no terminal.

-f-strings (f"..."): Utilizadas na exibição das mensagens (print) para inserir variáveis diretamente dentro do texto de forma limpa e legível.

-Operadores Lógicos (and / or): Utilizados na estrutura condicional (if/elif/else) para comparar a jogada do usuário contra a do computador e determinar o vencedor.

---
