# Importa o módulo re para usar expressões regulares
import re 

# Cria uma função para verificar a segurança de uma senha
def verificar_senha(senha):

    # Se a senha for menor que 8 caracteres, retorna uma mensagem de erro
    if len(senha) < 8: 
        return "Senha muito curta! A senha deve ter no mínimo 8 caracteres."
    
    # Se não houver pelo menos uma letra maiúscula, retorna uma mensagem de erro
    if not re.search(r"[A-Z]", senha):
        return "A senha deve conter pelo menos uma letra maiúscula."
    
    # Se não houver pelo menos uma letra minúscula, retorna uma mensagem de erro
    if not re.search(r"[a-z]", senha):
        return "A senha deve conter pelo menos uma letra minúscula."
    
    # Se não houver pelo menos um número, retorna uma mensagem de erro
    if not re.search(r"[0-9]", senha):
        return "A senha deve conter pelo menos um número."
    
    # Se não houver pelo menos um caractere especial, retorna uma mensagem de erro
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return "A senha deve conter pelo menos um caractere especial."
    
    # Se a senha atender a todos os critérios, retorna uma mensagem de sucesso
    return "Senha forte!"

# Pergunta pela senha até que ela seja forte
while True:
    senha_para_verificar = input("Digite uma senha para verificar: ")

    # Mostra o resultado da verificação da senha do usuário a partir da função verificar_senha()
    resultado = verificar_senha(senha_para_verificar)
    
    # Se a senha for forte, quebra o loop e sai
    if resultado == "Senha forte!":
        print(resultado)
        break
    else:
        print(resultado)
        print("Tente novamente.")