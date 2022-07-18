import json


# Função que exibe o menu de opções e funcionalidades do programa.
def menu_contatos():

    selecionar = input("Você acessou a lista de contatos dos Super-Heróis DC, selecione uma das opções:" "\n" + "<I> - Inserir novo contato" + "\n" +
                       "<P> - Pesquisar um contato" + "\n" + "<E> - Excluir um contato" + "\n" + "<V> - Visualizar lista completa" + "\n" + "Opção Selecionada: ").upper()

    return selecionar

#  Função que exibe todos os contatos existentes no nosso arquivos .JSON


def exibir_contatos():

    with open("R:\\OneDrive\\FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS\\3. MODELING\CODIGOS\\ListadeContatos_JSON\\listadecontatos.json", "r", encoding="UTF-8") as arquivo:

        listaDeContatos = arquivo.read()
        contatos = json.loads(listaDeContatos)

        for contato, infos in contatos.items():
            print(contato)
            for celular, email in infos.items():
                print(celular)
                print(email)

            print("\n")

    arquivo.close()


# Função para adicionar um novo contato no nosso arquivo .JSON. Ao final desta função o contato será salvo no arquivo.
def inserir():

    with open("R:\\OneDrive\\FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS\\3. MODELING\CODIGOS\\ListadeContatos_JSON\\listadecontatos.json", "r", encoding="UTF-8") as arquivo:
        listaDeContatos = arquivo.read()
        contatos = json.loads(listaDeContatos)

        novo_contato = input("Nome do novo contato: ")
        novo_celular = input("Número de celular: ")
        novo_email = input("E-mail do contato: ")

        contatos[novo_contato] = {"Celular": novo_celular, "Email": novo_email}

    arquivo = open("R:\\OneDrive\\FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS\\3. MODELING\CODIGOS\\ListadeContatos_JSON\\listadecontatos.json", "w", encoding="UTF-8")
    arquivo_final = json.dumps(contatos, indent=4)
    arquivo.write(arquivo_final)
    arquivo.close()

    print("Dados do novo contato armazenados com sucesso.")


# Função que irá pesquisar nome do contato no nosso arquivos JSON e retornar os valores de Celular e Email.
def pesquisar():

    with open("R:\\OneDrive\\FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS\\3. MODELING\CODIGOS\\ListadeContatos_JSON\\listadecontatos.json", "r", encoding="UTF-8") as arquivo:

        listaDeContatos = arquivo.read()
        contatos = json.loads(listaDeContatos)

        pesq_contato = input(
            "Informe o nome do contato que deseja pesquisar: ")
