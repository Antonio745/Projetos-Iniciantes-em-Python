def limpar_duplicados(lista):
    lista_limpa = list(set(lista))
    return lista_limpa

nomes =[
    "Ana", "Carlos", "Maria", "Pedro", "Ana", 
    "João", "Carlos", "Luiza", "Mariana", "Rafael", "Ana", "Carlos", "Bruna", "Eduardo", "Fernanda"
]
nomes_limpos = limpar_duplicados(nomes)
print(nomes_limpos)