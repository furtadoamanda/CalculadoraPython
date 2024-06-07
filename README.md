# Calculadora Python 🧮🐍

Criei este projeto para praticar os conteúdos aprendidos em Python.  
 É uma calculadora simples que realiza as operações de *adição*, *subtração*, *divisão*, *multiplicação* e *potencialização*.  

O código se inicia importando as funções que se encontram em um arquivo apartado, seguido por uma mensagem de boas-vindas e duas linhas de código que contribuem para o bom funcionamento do programa:

```python
from funcoes import *

print(f"{'*' * 10} CALCULADORA PYTHON {'*' * 10}")
running = True
selecao_valida = [1, 2, 3, 4, 5]
```
O trecho "running" indica que o código está em funcionamento e o laço de repetição será executado. Já a "selecao_valida" corresponde às possíveis seleções de operação.

O código é englobado em um bloco "try" para evitar que todo o programa quebre se ocorrer um *ValueError*, previsto para quando for inserido um caractere não numérico, tanto para a seleção da operação a ser realizada quanto para os números da operação.
➡️ Caso ocorra o erro definido, será exibida a mensagem "Valor não aceito" e o programa será encerrado.


### Parte inicial do código:
```python
operacao = """
        [1] - Adição
        [2] - Subtração
        [3] - Divisão
        [4] - Multiplicação
        [5] - Potencialização
        [0] - SAIR
        """
        print(operacao)
        selecao = int(input("> "))
        if selecao != 0 and selecao in selecao_valida:
            primeiro_numero = int(input("Primeiro numero: "))
            segundo_numero = int(input("Segundo numero: "))
```
Nessa parte do código, são apresentadas ao usuário as opções de operações possíveis, sendo ainda dada a oportunidade de sair e encerrar o programa.  
Se o usuário não inserir a opção para sair, bem como inserir um número válido dentre as opções, será pedido que insira os números a serem executados.

### Definição das funções:
```python
def adicao(primeiro_numero, segundo_numero):
    resultado = primeiro_numero + segundo_numero
    print(f"\t{primeiro_numero} + {segundo_numero} = {resultado}")
    print("***** Nova operação: ")

(...)
```
As funções das 5 operações que podem ser executadas são definidas no arquivo funcoes.py, sendo importadas no início do programa calculadora.py. Todas as funções possuem as mesmas funcionalidades, sendo definida a variável "resultado" e exibida a operação realizada. A seguir, é exibida uma nova frase de condução, uma vez que o código é realizado em um laço while.

### Bloco IF:
```python
if selecao == 1:
    adicao(primeiro_numero, segundo_numero)
elif selecao == 2:
    subtracao(primeiro_numero, segundo_numero)
elif selecao == 3:
    divisao(primeiro_numero, segundo_numero)
elif selecao == 4:
    multiplicacao(primeiro_numero, segundo_numero)
elif selecao == 5:
    potencializacao(primeiro_numero, segundo_numero)
elif selecao == 0:
    print("Saindo...")
    running = False
else:
    print("Seleção Inválida.")
```
Esse é o principal bloco do código, nele são executadas as funções de cada operação de acordo com a seleção feita pelo usuário.  
Os pontos principais são:
- Caso o usuário selecione a opção "0", que corresponde a "SAIR", a variável "running" é alterada para "False", o que encerra o laço while e encerra o programa.
- Caso o usuário insira um número que não corresponde a uma seleção válida, é exibida uma mensagem de invalidez.

