# Atividade 3: Cadastro de Livros para uma Biblioteca

total_livros = 0
total_novos = 0
livro_mais_antigo = ""
ano_mais_antigo = None

while True:
    # Entrada do título do livro
    titulo = input("Digite o título do livro: ")

    # Entrada e validação do ano de publicação
    ano = input("Digite o ano de publicação do livro: ")
    while not ano.isdigit() or int(ano) <= 0:
        print("Erro: Digite um número inteiro maior que zero.")
        ano = input("Digite o ano de publicação do livro: ")
    ano = int(ano)

    # Entrada e validação do estado do livro
    estado = input("Digite o estado do livro ('novo' ou 'usado'): ").lower()
    while estado != "novo" and estado != "usado":
        print("Erro: O estado do livro deve ser 'novo' ou 'usado'.")
        estado = input("Digite o estado do livro ('novo' ou 'usado'): ").lower()

    # Atualiza os contadores
    total_livros += 1
    if estado == "novo":
        total_novos += 1

    # Verifica se é o livro mais antigo
    if ano_mais_antigo is None or ano < ano_mais_antigo:
        ano_mais_antigo = ano
        livro_mais_antigo = titulo

    # Verifica se o usuário deseja continuar
    continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
    if continuar != 's':
        break

# Exibe os resultados
print("\n--- Resumo do Cadastro ---")
print(f"Total de livros cadastrados: {total_livros}")
print(f"Total de livros novos: {total_novos}")
print(f"Livro mais antigo: '{livro_mais_antigo}' (Publicado em {ano_mais_antigo})")
