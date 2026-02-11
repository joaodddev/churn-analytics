import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Deep Analytics", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0a0b10; color: #ffffff; }
    h1, h2 { color: #00d4ff !important; font-family: 'Orbitron', sans-serif; }
    .filter-box {
        background: #161b22;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00d4ff;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('/home/ubuntu/churn_dashboard/churn_data.csv')

df = load_data()

st.title("🔍 DEEP ANALYTICS")

# Filtros com estilo
with st.container():
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        sel_contrato = st.multiselect("Contratos", df['Contrato'].unique(), default=df['Contrato'].unique())
    with c2:
        sel_genero = st.multiselect("Gênero", df['Genero'].unique(), default=df['Genero'].unique())
    with c3:
        faixa_preco = st.slider("Mensalidade (R$)", 50, 200, (50, 200))
    with c4:
        churn_view = st.selectbox("Status Churn", ["Todos", "Sim", "Não"])
    
    # Aplicar filtros
    dff = df[
        (df['Contrato'].isin(sel_contrato)) & 
        (df['Genero'].isin(sel_genero)) &
        (df['Mensalidade'].between(faixa_preco[0], faixa_preco[1]))
    ]
    if churn_view != "Todos":
        dff = dff[dff['Churn'] == churn_view]
    st.markdown('</div>', unsafe_allow_html=True)

# --- GRID DE GRÁFICOS DA PÁGINA 2 ---
col1, col2 = st.columns(2)

with col1:
    # 5. Box Plot de Gastos Totais por Churn
    fig5 = px.box(dff, x="Churn", y="Total_Gasto", color="Churn",
                 title="💰 DISPERSÃO DE GASTO TOTAL",
                 color_discrete_map={'Sim': '#ff4b4b', 'Não': '#00d4ff'},
                 notched=True)
    fig5.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig5, use_container_width=True)

    # 6. Histograma de Idade (Overlay)
    fig6 = px.histogram(dff, x="Idade", color="Churn", marginal="rug",
                       title="👥 DISTRIBUIÇÃO ETÁRIA",
                       barmode="overlay",
                       color_discrete_map={'Sim': '#ff4b4b', 'Não': '#00d4ff'})
    fig6.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig6, use_container_width=True)

with col2:
    # 7. Scatter Plot 3D (Interatividade Máxima)
    fig7 = px.scatter_3d(dff, x='Idade', y='Mensalidade', z='Tempo_Meses',
                        color='Churn', size='Total_Gasto', opacity=0.7,
                        title="🌌 CLUSTERIZAÇÃO 3D DE CLIENTES",
                        color_discrete_map={'Sim': '#ff4b4b', 'Não': '#00d4ff'})
    fig7.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig7, use_container_width=True)

    # 8. Treemap de Segmentação
    fig8 = px.treemap(dff, path=[px.Constant("Base"), 'Contrato', 'Churn'], values='Mensalidade',
                     title="🌳 HIERARQUIA DE RISCO POR CONTRATO",
                     color='Churn', color_discrete_map={'Sim': '#ff4b4b', 'Não': '#00d4ff', '(?)': '#161b22'})
    fig8.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig8, use_container_width=True)

# Tabela de Dados Estilizada
st.markdown("### 📊 EXPLORADOR DE DADOS BRUTOS")
st.dataframe(dff.style.background_gradient(cmap='Blues', subset=['Mensalidade', 'Total_Gasto']), use_container_width=True)
