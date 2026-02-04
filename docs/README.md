# Documentação Economiza+ MVP

Este diretório contém a documentação do projeto.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `APRESENTACAO_PPT.md` | **Apresentação TCC (6 slides)** - Estrutura oficial |
| `APRESENTACAO_PPT.html` | Versão HTML da apresentação TCC |
| `APRESENTACAO.md` | Apresentação técnica em Markdown |
| `APRESENTACAO_SLIDES.md` | Versão para Marp (slides técnicos) |
| `APRESENTACAO.html` | Versão HTML da apresentação técnica |
| `RELATORIO_FINAL.md` | Relatório técnico completo |
| `RELATORIO_FINAL.html` | Relatório HTML (print to PDF) |
| `GUIA_DATASET_SINTETICO.md` | Documentação do dataset |

## Apresentação TCC (PPT)

A apresentação oficial do TCC segue a estrutura de 6 itens:

1. **Apresentação** - Quem é você
2. **Desafio** - Problema e hipóteses
3. **Solução** - Proposta e objetivo SMART
4. **Diferencial** - O que torna especial
5. **Desenvolvimento** - 3 Sprints (resumido)
6. **Resultados** - Métricas e lições aprendidas

### Gerando o PowerPoint

**Opção 1: Copiar do HTML (Recomendado)**

1. Abra `APRESENTACAO_PPT.html` no navegador
2. Crie um novo PowerPoint
3. Copie o conteúdo de cada "slide" do HTML para o PPT
4. Ajuste formatação conforme necessário

**Opção 2: Importar PDF para PPT**

1. Abra `APRESENTACAO_PPT.html` no navegador
2. `Ctrl+P` > "Salvar como PDF"
3. No PowerPoint: Inserir > Objeto > Criar do arquivo > PDF
4. Ou use um conversor online (smallpdf.com, ilovepdf.com)

**Opção 3: Via Pandoc**

```bash
# Instalar pandoc
sudo apt install pandoc

# Gerar PPTX
pandoc docs/APRESENTACAO_PPT.md -o docs/APRESENTACAO_TCC.pptx
```

## Gerando PDFs

### Relatório Final

1. Abra `RELATORIO_FINAL.html` no navegador
2. Pressione `Ctrl+P` (ou `Cmd+P` no Mac)
3. Selecione "Salvar como PDF"
4. Configure margens mínimas para melhor resultado

### Apresentação Técnica

#### Opção 1: Via HTML (Recomendado)

1. Abra `APRESENTACAO.html` no navegador
2. Pressione `Ctrl+P` (ou `Cmd+P` no Mac)
3. Selecione "Salvar como PDF"
4. Configure para paisagem se preferir slides

#### Opção 2: Via Marp CLI

```bash
# Instalar Marp CLI
npm install -g @marp-team/marp-cli

# Gerar PDF
marp docs/APRESENTACAO_SLIDES.md --pdf -o docs/APRESENTACAO.pdf
```

#### Opção 3: Via Pandoc

```bash
# Instalar pandoc
sudo apt install pandoc texlive-xetex  # Ubuntu/Debian

# Gerar PDF
pandoc docs/APRESENTACAO.md -o docs/APRESENTACAO.pdf
```

#### Opção 4: VS Code + Marp Extension

1. Instale a extensão "Marp for VS Code"
2. Abra `APRESENTACAO_SLIDES.md`
3. Clique no ícone de exportação
4. Selecione "Export slide deck (PDF)"

## Visualizando a Apresentação

Para visualizar como slides interativos:

```bash
# Com Marp CLI
marp docs/APRESENTACAO_SLIDES.md --server

# Acesse http://localhost:8080
```

## Conteúdo da Apresentação TCC

| Slide | Conteúdo |
|-------|----------|
| 1 | Apresentação pessoal (formação, experiência) |
| 2 | Desafio (problema, hipóteses, justificativa) |
| 3 | Solução (proposta, objetivo SMART) |
| 4 | Diferencial (6 pontos + stack) |
| 5 | Desenvolvimento (3 sprints + 4 perfis) |
| 6 | Resultados (validação, métricas, próximos passos) |
