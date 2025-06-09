"""   Cadastro de clientes e compras
1- O nome do cliente
2- O valor gasto pelo cliente (em reais)
3- A soma total dos valores gastos
4- O nome do cliente que mais gastou
REQUISITOS:
1- Utilizar o while para repetir o cadastro
2- Validar a entrada com .isdigit()
3- Contabilizar o número total de clientes cadastrados
4- Mostrar o nome do cliente que mais gastou
"""

print(" ----- CADASTRO DE CLIENTES E COMPRAS ----- ")

total_gasto = 0
cliente_que_mias_gastou = ""
maior_valor_gasto = 0
quantidade = 0

while True:
    nome = input("\n Digite o nome do cliente: ")
    valor = int(input("\n Digite o valor gasto pelo cliente (em reais): "))

    while not valor.isdigit():
        print("Valor inválido. Digite apenas números inteiros.")
        valor = input("\n Digite o valor gasto pelo cliente (em reais): ")
    valor = int(valor)

    total_gasto += valor
    quantidade += 1
    if valor > maior_valor_gasto:
        maior_valor_gasto = valor
        cliente_que_mais_gastou = nome

    continuar = input("\n Deseja continuar o cadastro? (s/n): ").upper()
    if continuar != "S":
        break

print("\n --- Resumo do cadastro --- ")
print(f"Total de clientes cadastrados: {quantidade}")
print(f"Total gasto pelos clientes: R$ {total_gasto:.2f}")
print(f"Cliente que mais gastou: {cliente_que_mais_gastou} (R$ {maior_valor_gasto:.2f})")