# Importa o módulo secrets para gerar senhas aleatórias
import secrets
# Importa o módulo string para usar caracteres especiais
import string

# Cria uma função para gerar uma senha forte
def gerar_senha(tamanho=int(input("Digite o tamanho da senha: "))):
    
    # Define os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha aleatória com base nos caracteres possíveis e no tamanho informado pelo usuário
    # Para cada um dos caracteres, escolhe um caractere aleatório da lista de caracteres e junta todos em uma única string sem ter espaço
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    return senha

# Gerar e exibir uma senha forte a partir da função gerar_senha() com o tamanho informado pelo usuário 
senha_gerada = gerar_senha()
print(f"Senha gerada: {senha_gerada}")