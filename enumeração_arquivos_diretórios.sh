#!/bin/bash

# Solicita ao usuário o diretório de origem
echo "Digite o caminho do diretório de origem para buscar arquivos ocultos:"
read DIRETORIO_ORIGEM

# Verifica se o diretório de origem existe
if [ ! -d "$DIRETORIO_ORIGEM" ]; then
  echo "O diretório informado não existe. Verifique o caminho e tente novamente."
  exit 1
fi

# Diretório para armazenar os logs
LOG_DIR="/home/nicks/logs/logs_enum"
mkdir -p "$LOG_DIR"

# Nome do arquivo de log com base na data atual
LOG_FILE="$LOG_DIR/enum_$(date +"%d-%m-%Y_%H-%M-%S").log"

# Função para listar arquivos e diretórios ocultos
enum_arquivos_ocultos() {
    echo "[$(date)] Iniciando enumeração de arquivos e diretórios ocultos em $DIRETORIO_ORIGEM" >> "$LOG_FILE"
    echo "Arquivos e diretórios ocultos encontrados:" >> "$LOG_FILE"
    
    # Lista arquivos e diretórios ocultos, incluindo subdiretórios
    find "$DIRETORIO_ORIGEM" -name ".*" -type f >> "$LOG_FILE"
    find "$DIRETORIO_ORIGEM" -name ".*" -type d >> "$LOG_FILE"
    
    echo "[$(date)] Enumeração concluída. Relatório salvo em $LOG_FILE" >> "$LOG_FILE"
}

# Chama a função de enumeração
enum_arquivos_ocultos

# Exibe a mensagem de sucesso
echo "A enumeração foi concluída com sucesso. O relatório foi salvo em $LOG_FILE"
