"""  Controle de veículos de uma garagem
    1- O modelo do veículo
    2- O numero de dias que o veículo ficará na garagem(validar o numero de dias)
    3- AA soma de dias de todos os veículos
    4- O modelo de veeículo que ficará mais tempo na garagem
    REQUISITOS:
    1- Utilizar o while para repetir o cadastro
    2- Validar a entrada com .isdigit()
    3- Contabilizar o numero total de veículos
    4- Calcular a média de dias dos veículos
    5- Mostrar qual é o veículo que ficará mais tempo
"""
print(" ----- CONTROLE DE VEÍCULOS DE GARAGEM ----- ")

total_dias = 0
total_veiculos = 0
veiculo_mais_tempo = ""
mais_dias = 0

while True:
    modelo = input("Informe o modelo do veículo: ")

    dias = input("Informe o número de dias que o veículo ficará estacionado: ")
    while not dias.isdigit():
        print("Valor inválido. Digite apenas números inteiros.")
        dias = input("Informe o número de dias que o veículo ficará estacionado: ")
    
    dias = int(dias)

    # Atualizando estatísticas
    total_dias += dias
    total_veiculos += 1

    if dias > mais_dias:
        mais_dias = dias
        veiculo_mais_tempo = modelo

    # Perguntar ao usuário se deseja continuar
    continuar = input("Deseja cadastrar outro veículo? (s/n): ").lower()
    if continuar != 's':
        break

print("\nResumo dos Cadastros:")
print(f"Total de veículos cadastrados: {total_veiculos}")
print(f"Soma total de dias de todos os veículos: {total_dias}")
print(f"Média de dias de permanência: {total_dias / total_veiculos:.2f}")
print(f"O veículo que ficará mais tempo na garagem é: {veiculo_mais_tempo} ({mais_dias} dias)")