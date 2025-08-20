# 📊 EDA - Análise Exploratória de Dados

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flet](https://img.shields.io/badge/Flet-0.28+-green.svg)](https://flet.dev/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-orange.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Uma aplicação desktop moderna e intuitiva para análise exploratória de dados (EDA) construída com Flet e Python.**

## 🚀 Sobre o Projeto

O **EDA App** é uma ferramenta desktop que permite aos usuários realizar análises exploratórias de dados de forma simples e visual. Com uma interface moderna construída em Flet, você pode analisar arquivos CSV diretamente de URLs ou arquivos locais, obtendo insights valiosos sobre seus dados.

### ✨ Características Principais

- 🎯 **Interface Intuitiva**: Design moderno e responsivo com Flet
- 📊 **Análise Automática**: Estatísticas descritivas, tipos de dados e valores nulos
- 🔍 **Prévia dos Dados**: Visualização das primeiras linhas em tabela
- 📈 **Múltiplos Separadores**: Suporte para vírgula, ponto e vírgula, tabulação e pipe
- 🌐 **URL Direta**: Análise de arquivos CSV hospedados na web
- 📱 **Responsivo**: Funciona em diferentes tamanhos de tela
- 🎨 **Tema Claro**: Interface limpa e profissional

## 🖼️ Screenshots

### Interface Principal
![Interface Principal](https://via.placeholder.com/800x500/4A90E2/FFFFFF?text=Interface+Principal+do+EDA+App)

### Análise de Dados
![Análise](https://via.placeholder.com/800x500/50C878/FFFFFF?text=Resultados+da+Análise)

### Prévia dos Dados
![Prévia](https://via.placeholder.com/800x500/FF6B35/FFFFFF?text=Prévia+dos+Dados)

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Flet 0.28+** - Framework para aplicações desktop
- **Pandas 2.0+** - Manipulação e análise de dados
- **Requests** - Download de arquivos da web
- **Plotly** - Visualizações interativas (futuro)

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/eduardoml93/python-flet-App-EDA.git
cd eda-app
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv dundunapp
dundunapp\Scripts\activate

# Linux/Mac
python3 -m venv dundunapp
source dundunapp/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o aplicativo

```bash
python app.py
```

## 📖 Como Usar

### 1. **Iniciar o App**
Execute o aplicativo e uma janela será aberta com a interface principal.

### 2. **Configurar a Análise**
- **URL do CSV**: Cole o link direto para o arquivo CSV
- **Separador**: Selecione o separador usado no arquivo (vírgula, ponto e vírgula, etc.)

### 3. **Analisar Dados**
Clique em "🔍 Analisar Dados" para iniciar o processo de análise.

### 4. **Explorar Resultados**
O app irá mostrar:
- 📋 **Informações Básicas**: Total de registros, colunas e tamanho
- 🔍 **Tipos de Dados**: Tipos de cada coluna
- 📈 **Estatísticas Descritivas**: Média, mediana, desvio padrão, etc.
- 🏷️ **Análise Categórica**: Valores únicos e frequências
- ⚠️ **Valores Nulos**: Identificação de dados faltantes
- 👁️ **Prévia dos Dados**: Primeiras 10 linhas em tabela

## 📊 Exemplo de Uso

### Dataset do Titanic
O app vem configurado com o dataset do Titanic como exemplo:

```
https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv
```

Este dataset contém informações sobre passageiros do Titanic, incluindo:
- **PassengerId**: ID único do passageiro
- **Survived**: Se sobreviveu (0=Não, 1=Sim)
- **Pclass**: Classe da passagem (1=Primeira, 2=Segunda, 3=Terceira)
- **Name**: Nome do passageiro
- **Sex**: Gênero
- **Age**: Idade
- **SibSp**: Número de irmãos/cônjuges a bordo
- **Parch**: Número de pais/filhos a bordo
- **Ticket**: Número do bilhete
- **Fare**: Tarifa da passagem
- **Cabin**: Número da cabine
- **Embarked**: Porto de embarque

## 🔧 Estrutura do Projeto

```
eda-app/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── .gitignore            # Arquivos ignorados pelo Git
└── dundunapp/            # Ambiente virtual (não versionado)
    ├── Lib/
    ├── Scripts/
    └── pyvenv.cfg
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.



⭐ **Se este projeto te ajudou, considere dar uma estrela no GitHub!**

**Made with ❤️ and ☕ by Eduardo ML**
