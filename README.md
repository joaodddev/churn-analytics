# 🌌 Churn Insight - Deep Dark Analytics

![Status](https://img.shields.io/badge/Status-Completo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-FF4B4B)

Um dashboard de análise de Churn ultra-moderno desenvolvido com **Python**, **Pandas** e **Streamlit**. Este projeto foca em uma estética "Deep Dark" com visualizações avançadas e interatividade de alto nível para insights estratégicos de retenção de clientes.

## 🚀 Funcionalidades

- **Design Premium:** Interface em Dark Mode com estética neon e fontes futuristas.
- **Arquitetura Multi-Páginas:** Separação clara entre Visão Executiva e Análise Detalhada.
- **Visualizações Avançadas:**
  - Gráficos de Área Neon para tendências.
  - **Scatter Plot 3D Interativo** para clusterização de clientes.
  - Radar Charts para perfis psicográficos.
  - Heatmaps e Treemaps para segmentação de risco.
- **Filtros Dinâmicos:** Controle total sobre a base de dados em tempo real.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Manipulação de Dados:** Pandas & Numpy
- **Visualização:** Plotly Express & Graph Objects
- **Framework Web:** Streamlit
- **Estilização:** CSS Customizado (Glassmorphism)

## 📂 Estrutura do Projeto

```text
├── app.py                # Página Principal (Home)
├── pages/
│   └── 1_Detalhes.py     # Página de Análise Detalhada
├── .streamlit/
│   └── config.toml       # Configurações de Tema Dark
├── data_generator.py     # Script para gerar dados fictícios
├── churn_data.csv        # Dataset gerado
└── requirements.txt      # Dependências do projeto
```

## 🔧 Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/churn-insight-pro.git
   cd churn-insight-pro
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   streamlit run app.py
   ```

---
Desenvolvido com ❤️ para fins de portfólio.
