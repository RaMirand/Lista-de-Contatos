import json

from numpy import insert
from functions import *

opcao = menu_contatos()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "V":

    if opcao == "I":
        inserir()

    elif opcao == "P":
        pesquisar()

    elif opcao == "V":
        exibir_contatos()

    opcao = menu_contatos()
