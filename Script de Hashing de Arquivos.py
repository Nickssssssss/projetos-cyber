import hashlib # Módulo para cálculo de hashes

def calcular_hash(arquivo, algoritmo="sha256"): 
    """Calcula o hash de um arquivo."""
    try:
        hash_objeto = hashlib.new(algoritmo) # Cria um objeto de hash com o algoritmo especificado
        with open(arquivo, "rb") as f: # Abre o arquivo em modo binário
            while chunk := f.read(8192):  # Lê o arquivo em partes de 8 KB para evitar consumo excessivo de memória
                hash_objeto.update(chunk) # Atualiza o hash com a parte lida
        return hash_objeto.hexdigest() # Retorna o hash em hexadecimal
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except ValueError:
        return f"Erro: Algoritmo '{algoritmo}' não suportado."

def main():
    # Solicita o caminho do arquivo e o algoritmo de hashing
    arquivo = input("Digite o caminho do arquivo: ")
    algoritmo = input("Digite o algoritmo de hash (md5, sha1, sha256): ").lower() 
    
    # Calcula e exibe o hash do arquivo
    hash_calculado = calcular_hash(arquivo, algoritmo) 
    print(f"Hash ({algoritmo}): {hash_calculado}") 
    
    # Verifica integridade, se o usuário quiser
    if "Erro" not in hash_calculado:
        opcao = input("Deseja verificar integridade? (s/n): ").lower()
        if opcao == "s":
            hash_original = input("Digite o hash original: ")
            if hash_calculado == hash_original:
                print("O arquivo está íntegro.")
            else:
                print("O arquivo foi alterado!")

main() # Chama a função principal