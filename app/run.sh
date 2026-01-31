#!/bin/bash
# Script para executar o dashboard Economiza+ MVP
# Uso: ./run.sh

echo "==================================="
echo "  Economiza+ MVP Dashboard"
echo "==================================="
echo ""

# Verificar se streamlit esta instalado
if ! command -v streamlit &> /dev/null; then
    echo "Streamlit nao encontrado. Instalando..."
    pip install streamlit plotly
fi

echo "Iniciando dashboard..."
echo "Acesse: http://localhost:8501"
echo ""

# Executar streamlit
streamlit run app.py --server.headless=true
