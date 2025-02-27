#!/bin/bash

# Solicita ao usuário os diretórios de origem e destino
echo "Digite o caminho do diretório de origem (onde os arquivos a serem copiados estão localizados):"
read ORIGEM

# Diretório fixo de destino para armazenar os backups
DESTINO="/home/nicks/backups_feitos"
mkdir -p "$DESTINO"  # Cria o diretório de destino caso não exista

# Diretório para armazenar os logs
LOG_DIR="/home/nicks/logs/logs_backups"
mkdir -p "$LOG_DIR"

# Nome do arquivo de log com base na data atual
LOG_FILE="$LOG_DIR/backup_$(date +"%d-%m-%Y_%H-%M-%S").log"

# Data e hora atual para a criação do backup
DATA_ATUAL=$(date +"%d-%m-%Y_%H-%M-%S")

# Nome do arquivo de backup
NOME_BACKUP="backup_${DATA_ATUAL}.tar.gz"

# Nome do arquivo criptografado (com extensão .gpg)
NOME_BACKUP_CRIPT="backup_${DATA_ATUAL}.tar.gz.gpg"

# Senha para criptografia
echo "Digite a senha para criptografar o backup:"
read -s SENHA  # O -s oculta a entrada da senha

# Função para fazer o backup
backup() {
    # Log do início do processo
    echo "[$(date)] Iniciando backup..." >> "$LOG_FILE"

    # Verificando se a origem é um arquivo ou diretório
    if [ -f "$ORIGEM" ]; then
        # Se for um arquivo, usamos diretamente o arquivo para o backup
        tar -czf "$DESTINO/$NOME_BACKUP" "$ORIGEM"
    elif [ -d "$ORIGEM" ]; then
        # Se for um diretório, usamos o diretório para o backup
        tar -czf "$DESTINO/$NOME_BACKUP" -C "$ORIGEM" .
    else
        echo "[$(date)] Erro: A origem não é um arquivo nem um diretório válido." >> "$LOG_FILE"
        echo "Erro ao fazer backup: A origem não é um arquivo nem um diretório válido."
        exit 1
    fi

    # Verificando se o backup foi criado corretamente
    if [ $? -eq 0 ]; then
        echo "[$(date)] Backup criado: $NOME_BACKUP" >> "$LOG_FILE"
    else
        echo "[$(date)] Erro ao criar o backup." >> "$LOG_FILE"
        echo "Erro ao fazer backup."
        exit 1
    fi

    # Criptografando o backup com GPG (utilizando uma senha)
    gpg --batch --yes --passphrase "$SENHA" -c "$DESTINO/$NOME_BACKUP"

    # Verificando se a criptografia foi bem-sucedida
    if [ $? -eq 0 ]; then
        echo "[$(date)] Backup criptografado: $NOME_BACKUP_CRIPT" >> "$LOG_FILE"
        rm "$DESTINO/$NOME_BACKUP"  # Remove o arquivo não criptografado para segurança
    else
        echo "[$(date)] Erro ao criptografar o backup." >> "$LOG_FILE"
        echo "Erro ao criptografar o backup."
        exit 1
    fi

    # Log do término do processo
    echo "[$(date)] Backup concluído." >> "$LOG_FILE"

    # Mensagem de sucesso
    echo "Backup concluído com sucesso e salvo no diretório $DESTINO"
}

# Função principal
main() {
    backup
}

# Chama a função principal
main

#Para visualizar o conteúdo do arquivo/diretório criptografado, é preciso descriptografar com o comando
#gpg --decrypt backup_20-01-2025_17-34-58.tar.gz.gpg | tar -tzf -
#Assim ira ficar de forma temporária no sistema o arquivo descriptografado

#Ou então gpg --decrypt --passphrase YOUR_PASSWORD backup_20-01-2025_17-34-58.tar.gz.gpg > backup_20-01-2025_17-34-58.tar.gz
#e em seguida tar -tf backup_20-01-2025_17-34-58.tar.gz para verificar o conteúdo do arquivo/diretório. 
#Porém dessa forma fica armazenado no sistema o arquivo/diretório descriptografado.
