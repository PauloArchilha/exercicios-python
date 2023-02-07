import os


lista_compra = []

while True:
    print('Selecione uma opção!')
    opcao = input('[i]nserir  [a]pagar  [l]istar: ').casefold()

    # adicionar na lista
    if opcao == 'i':
        os.system('clear')
        produto = input('Digite o produto: ').capitalize()
        lista_compra.append(produto)
        print(f'\033[92m{produto}\033[0m adicionado!')

    # apagar da lista
    elif opcao == 'a':
        if len(lista_compra) == 0:
            print('Você não possui itens na sua lista para apagar!')
        else:
            apagar_produto = input(
                'Digite o numero do item que deseja apagar: ')
            try:
                apagar_produto = int(apagar_produto) - 1
                item_removido = lista_compra.pop(apagar_produto)
                print(f'\033[91m{item_removido}\033[0m apagado da lista')
            except ValueError:
                print('Você digitou uma letra, por favor digite um número!')
            except IndexError:
                print('Indice não encontrado')

    # listar itens da lista
    elif opcao == 'l':
        if len(lista_compra) == 0:
            print('Lista vazia!')
        for i, item in enumerate(lista_compra):
            print(f'\033[94m{i+1}. {item}\033[0m')

    elif 'q' in opcao:
        print('Fechando a lista!')
        break
    else:
        print('Por favor, escolha uma das opções!')
