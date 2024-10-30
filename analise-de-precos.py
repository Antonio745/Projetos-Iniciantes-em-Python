# Lista de produtos com preços
produtos_precos = [
    {"produto": "motores elétricos", "preco": 1500.00},
    {"produto": "compressores de ar", "preco": 2500.70},
    {"produto": "bombas hidráulicas", "preco": 1800.49},
    {"produto": "rolamentos e mancais", "preco": 100.00},
    {"produto": "válvulas industriais", "preco": 300.00},
    {"produto": "transformadores de energia", "preco": 5000.00},
    {"produto": "correias e polias", "preco": 200.50},
    {"produto": "controladores e sensores", "preco": 800.00},
    {"produto": "máquinas cnc", "preco": 15000.00},
    {"produto": "placas de circuito impresso (pcb)", "preco": 50.99},
    {"produto": "motores de passo", "preco": 350.89}  
]
#da lista acima extraia somente os preços

precos = [item["preco"] for item in produtos_precos]
print(precos)

#some os preços
total = sum(precos)
#dê um desconto de 5% no valor total
desconto = total * 0.05
total_com_desconto = total - desconto
#exiba o valor total, o valor do desconto, e o valor total com desconto
print(f"valor total : R${total:.2f}")
print(f"desconto de 5% : R${desconto:.2f}")
print(f"valor total com desconto : R${total_com_desconto:.2f} ")
