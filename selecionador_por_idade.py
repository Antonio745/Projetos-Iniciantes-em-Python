# O desafio é extrair de um banco de dados pessoas com idade igual ou acima de 40 anos
pessoas = {
    "Ana": 24,
    "Bruno": 32,
    "Carlos": 18,
    "Diana": 27,
    "Eduardo": 45,
    "Fernanda": 30,
    "Gabriel": 22,
    "Helena": 29,
    "Igor": 34,
    "Juliana": 19,
    "Lucas": 40,
    "Mariana": 26,
    "Nathan": 31,
    "Olivia": 23,
    "Paulo": 50,
    "Raquel": 36,
    "Samuel": 28,
    "Tatiane": 21,
    "Vinícius": 33,
    "Yasmin": 25
}

# Faça uma lista para armazenar candidatos com 40 anos ou mais
pessoas_40_ou_mais={}

# Selecione candidatos com idade >= 40
for nome,idade in pessoas.items():
    if idade >= 40:
        pessoas_40_ou_mais[nome] = idade

# Exibindo os candidatos selecionados
for nome, idade in pessoas_40_ou_mais.items():
    print(f"{nome}: {idade} anos")