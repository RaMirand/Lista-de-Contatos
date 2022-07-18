import json

contatos = contatos = {
    "Clark Kent":
        {"Celular": "11985423674",
         "Email": "clark@krypton.com"},
    "Bruce Wayne":
        {"Celular": "11978965312",
         "Email": "brucewayne@batcaverna.com"}
}

final = json.dumps(contatos, indent=4)

print(final)

arquivo = open("R:\\OneDrive\\FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS\\3. MODELING\CODIGOS\\ListadeContatos_JSON\\listadecontatos.json", "w")
arquivo.write(final)
arquivo.close
