#!/usr/bin/env bash

QUANTIDADE=${1:-4}
SUB_DIR=${2:-"./M02"}
PREFIXO=${3:-"ex"}

echo "Criando $QUANTIDADE diretorios em '$SUB_DIR'..."
mkdir "${SUB_DIR}"
for (( i = 1; i <= QUANTIDADE; i++ )); do
    NOME_DIR="${SUB_DIR}/${PREFIXO}${i}"
    
    mkdir -p "$NOME_DIR"
    touch "${NOME_DIR}/arq.py"
done

echo "Concluído!"
