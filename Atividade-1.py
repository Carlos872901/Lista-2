"""   CADASTRO DE ALUNOS E NOTAS
   1- O nome do aluno
   2- A nota final do aluno
   3- A soma total das notas
   4- O nome do aluno com a maior nota
   REQUISITOS:
   1- Utilizar o while para repetir o cadastro
   2- Validar a entrada com .isdigit()
   3- Contabilizar o numero total de alunos
   4- Calcular a média das notas
   5- Mostrar qual e o aluno com a maior nota
"""
print(" ----- CADASTRO DE ALUNOS E NOTA -----  ")

total_notas = 0
maior_nota = -1
aluno_maior_nota = ""
total_alunos = 0

while True:

    nome = input("\n Digite o nome do aluno: ")
    nota_input = input(f"\n Digite a nota final de {nome}: ")

    while not nota_input.isdigit():
        print("Erro: a nota deve ser um número inteiro.")
        nota_input = input(f"Digite a nota final de {nome}: ")

    nota = int(nota_input)

    total_notas += nota
    total_alunos += 1


    if nota > maior_nota:
        maior_nota = nota
        aluno_maio_nota = nome

    continuar = input("\n Deseja continuar? (s/n): ").strip().upper()
    if continuar != "S":
        break

print("\n --- FIM DO CADASTRO --- ")
print(f"Total de alunos: {total_alunos}")
print(f"Média das notas: {total_notas / total_alunos:.2f}")
print(f"Aluno com a maior nota: {aluno_maior_nota}")
