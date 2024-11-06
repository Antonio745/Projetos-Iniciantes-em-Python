velocidade_permitida = 80
velocidade_do_veiculo = int(input("Qual a velocidade do veículo: "))

if velocidade_do_veiculo > velocidade_permitida:
    print("Você foi multado!!")
    valor_da_multa = (velocidade_do_veiculo - velocidade_permitida) * 10
    print(f'Sua multa é de R${valor_da_multa:.2f}')
else:
    print("Dirija com cuidado")