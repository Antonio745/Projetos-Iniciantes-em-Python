# Sistema de Login com Senha de 6 Números

def solicitar_senha():
    senha = input("Digite sua senha de 6 números: ")
    return senha

def verificar_senha(senha):  # A função deve receber 'senha' como argumento
    # Verifica se a senha tem 6 caracteres e se todos são dígitos
    if len(senha) == 6 and senha.isdigit():
        return True
    return False  # Retornar False fora da condição

def main():
    senha = solicitar_senha()
    if verificar_senha(senha):
        print("Login bem-sucedido.")
    else:
        print("Senha inválida, a senha deve ter 6 números.")

# Executa o programa
if __name__ == "__main__": 
    main()
