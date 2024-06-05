print(f"{'*' * 10} CALCULADORA PYTHON {'*' * 10}")
running = True
selecao_valida = [1, 2, 3, 4, 5]

try:
    while running:
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

        def adicao(primeiro_numero, segundo_numero):
            resultado = primeiro_numero + segundo_numero
            print(f"\t{primeiro_numero} + {segundo_numero} = {resultado}")
            print("***** Nova operação: ")


        def subtracao(primeiro_numero, segundo_numero):
            resultado = primeiro_numero - segundo_numero
            print(f"\t{primeiro_numero} - {segundo_numero} = {resultado}")
            print("***** Nova operação: ")


        def divisao(primeiro_numero, segundo_numero):
            resultado = primeiro_numero / segundo_numero
            print(f"\t{primeiro_numero} / {segundo_numero} = {resultado}")
            print("***** Nova operação: ")


        def multiplicacao(primeiro_numero, segundo_numero):
            resultado = primeiro_numero * segundo_numero
            print(f"\t{primeiro_numero} x {segundo_numero} = {resultado}")
            print("***** Nova operação: ")


        def potencializacao(primeiro_numero, segundo_numero):
            resultado = primeiro_numero ** segundo_numero
            print(f"\t{primeiro_numero} ** {segundo_numero} = {resultado}")
            print("***** Nova operação: ")


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

except ValueError:
    print("Valor não aceito.")
