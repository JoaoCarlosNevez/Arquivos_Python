def criar_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    conteudo = input("Digite o conteúdo para o arquivo: ")

    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
            print("Arquivo criado e conteúdo gravado com sucesso!")
    except IOError:
        print("Erro ao criar o arquivo.")

# Ler o conteúdo de um arquivo
def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")

    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except IOError:
        print("Erro ao ler o arquivo.")

# Copiar o conteúdo de um arquivo para outro
def copiar_arquivo():
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    arquivo_destino = input("Digite o nome do arquivo de destino: ")

    try:
        with open(arquivo_origem, 'r') as origem:
            with open(arquivo_destino, 'w') as destino:
                conteudo = origem.read()
                destino.write(conteudo)
            print("Arquivo copiado com sucesso!")
    except IOError:
        print("Erro ao copiar o arquivo.")

# Menu principal
def menu():
    while True:
        print("\nManipulação de Arquivos")
        print("1. Criar arquivo e escrever nele")
        print("2. Ler conteúdo de um arquivo")
        print("3. Copiar conteúdo de um arquivo para outro")
        print("0. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            criar_arquivo()
        elif opcao == '2':
            ler_arquivo()
        elif opcao == '3':
            copiar_arquivo()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

# Executar o programa
menu()