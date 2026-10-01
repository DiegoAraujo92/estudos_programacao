import os
lista = []
opcao = ''
while True:
       
    print("Selecione uma opção\n")
    opcao = input("[i]inserir [r]remover [c]limpar [l]listar [s]sair\n")

    while opcao == "i":
        os.system("cls")
        valor = input("Digite um item: ")
        lista.append(valor)       
        if valor == 'sair'and lista.pop():
                break
        
    if len(opcao) > 1:
        os.system("cls")
        print("Por favor, digite apenas uma letra.")
    #elif opcao == "i":
    #   valor = input("Digite um item: ")
    #   lista.append(valor)
    
    elif opcao == 'c':
        lista.clear()
    
    elif opcao == "r":
        os.system("cls")
        try:
            indice_str = int(input("qual item deseja remover: "))
            indice = indice_str
            del lista[indice]
        except:
            print()

    elif opcao == "l":
        os.system("cls") 
        if len(lista) == 0:
            print("A lista está vazia.")
        for i, item in enumerate(lista, start=0):
            print(f"{i}. {item}")

    elif opcao == "s":
        break
    
