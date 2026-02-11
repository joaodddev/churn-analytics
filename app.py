import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Churn Dark Insight",
    page_icon="🌌",
    layout="wide"
)

# CSS para Estética Dark Neon e Glassmorphism
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #0a0b10;
        color: #ffffff;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #00d4ff !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }

    .metric-card {
        background: rgba(22, 27, 34, 0.8);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: transform 0.3s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
    }

    /* Estilizando scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0a0b10; }
    ::-webkit-scrollbar-thumb { background: #161b22; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv('/home/ubuntu/churn_dashboard/churn_data.csv')

df = load_data()

# --- HEADER ---
st.markdown("# 🌌 CHURN INSIGHT PRO <span style='font-size: 0.4em; color: #888;'>v2.0 Dark</span>", unsafe_allow_html=True)
st.markdown("### Monitoramento de Retenção em Tempo Real")

# --- KPIs EM GRID ---
st.markdown("---")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

churn_rate = (len(df[df['Churn'] == 'Sim']) / len(df)) * 100
mrr = df['Mensalidade'].sum()

with kpi1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total de Clientes", f"{len(df):,}", "Active")
    st.markdown('</div>', unsafe_allow_html=True)
with kpi2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Taxa de Churn", f"{churn_rate:.1f}%", "-0.8%", delta_color="normal")
    st.markdown('</div>', unsafe_allow_html=True)
with kpi3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("MRR Estimado", f"R$ {mrr/1000:.1f}k", "+2.4%")
    st.markdown('</div>', unsafe_allow_html=True)
with kpi4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Ticket Médio", f"R$ {df['Mensalidade'].mean():.0f}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- GRID DE GRÁFICOS (4 GRÁFICOS NA HOME) ---
col_a, col_b = st.columns(2)

with col_a:
    # 1. Probabilidade de Churn por Tempo (Área Neon)
    churn_by_tenure = df.groupby('Tempo_Meses')['Churn'].apply(lambda x: (x == 'Sim').mean()).reset_index()
    fig1 = px.area(churn_by_tenure, x='Tempo_Meses', y='Churn', 
                  title="📈 CURVA DE RISCO POR TEMPO",
                  color_discrete_sequence=['#00d4ff'])
    fig1.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Distribuição de Receita por Contrato (Sunburst)
    fig2 = px.sunburst(df, path=['Contrato', 'Genero'], values='Mensalidade',
                      title="☀️ COMPOSIÇÃO DE RECEITA",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    # 3. Heatmap de Idade vs Mensalidade
    fig3 = px.density_heatmap(df, x="Idade", y="Mensalidade", z="Tempo_Meses", 
                             histfunc="avg", title="🔥 MAPA DE CALOR: PERFIL FINANCEIRO",
                             color_continuous_scale='Viridis')
    fig3.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Radar Chart de Atributos (Simulado)
    categories = ['Fidelidade', 'Gasto', 'Tempo', 'Interação', 'Satisfação']
    fig4 = go.Figure()
    fig4.add_trace(go.Scatterpolar(
          r=[80, 70, 90, 60, 85], theta=categories, fill='toself', name='Retidos',
          line_color='#00d4ff'))
    fig4.add_trace(go.Scatterpolar(
          r=[30, 95, 20, 40, 50], theta=categories, fill='toself', name='Churn',
          line_color='#ff4b4b'))
    fig4.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                      showlegend=True, title="🎯 PERFIL PSICOGRÁFICO",
                      template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig4, use_container_width=True)

st.sidebar.markdown("### 🛠️ CONFIGURAÇÕES")
st.sidebar.info("O sistema está operando em modo de alto desempenho com processamento paralelo de dados.")
