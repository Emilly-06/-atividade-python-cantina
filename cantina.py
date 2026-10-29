# menu usando while
# usar if para escolhas
# cada escolha acrescenta valor da compra
# contar a quantidade de produtos comprados
valort = 0
quantp = 0
opcao = 0
while opcao != 4:
    print("\nOpção -- Produto -- Preço")
    print(" [1]  --   Suco  -- R$5,00")
    print(" [2]  -- Salgado -- R$7,00")
    print(" [3]  --Sanduíche-- R$10,00")
    print(" [4] Finalizar compra")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # suco
        valort += 5
        quantp += 1
        print('\nValor total = {}'.format(valort))
        print('Quantidade total = {}'.format(quantp))
    elif opcao == 2:
        # salgado
        valort += 7
        quantp += 1
        print('\nValor total = {}'.format(valort))
        print('Quantidade total = {}'.format(quantp))
    elif opcao == 3:
        # sanduiche
        valort += 10
        quantp += 1
        print('\nValor total = {}'.format(valort))
        print('Quantidade total = {}'.format(quantp))
    elif opcao == 4:
        print('\nFinalizando compra:')
        print('Valor total = {}'.format(valort))
        print('Quantidade total = {}'.format(quantp))
    else:
        print('\033[31m\nOpção invalida.\033[00m')