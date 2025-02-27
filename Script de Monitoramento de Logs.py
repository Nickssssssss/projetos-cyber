import time # Importa a biblioteca time para usar a função sleep()
import re # Importa o módulo re para usar expressões regulares

def monitorar_logs(caminho_log, padrao_monitorado): # Define a função monitorar_logs() com dois parâmetros de entrada 
    try:
        with open(caminho_log, "r") as arquivo: # Abre o arquivo de log em modo de leitura
            arquivo.seek(0, 2) # Move o cursor para o final do arquivo
            print(f"Monitorando o arquivo: {caminho_log}") # Exibe o caminho do arquivo sendo monitorado
            
            while True:
                linha = arquivo.readline() # Lê uma linha do arquivo
                if not linha:
                    # Aguarda por novas linhas
                    time.sleep(1)
                    continue

                # Verifica se a linha corresponde ao padrão de busca
                if re.search(padrao_monitorado, linha):
                    print(f"ALERTA: {linha.strip()}") # Exibe a linha que corresponde ao padrão de busca
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_log}' não foi encontrado.")
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")

def main():
    # Solicita o caminho do arquivo de log
    caminho_log = input("Digite o caminho do arquivo de log: ")
    
    # Solicita o padrão de busca
    padrao_monitorado = input("Digite o padrão a ser monitorado (exemplo: 'ERROR', 'WARNING'): ")
    
    # Inicia o monitoramento
    monitorar_logs(caminho_log, padrao_monitorado)
 
main() # Chama a função principal  
