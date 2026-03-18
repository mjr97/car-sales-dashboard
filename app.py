import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas de Carros", layout="wide")

# Carregando os dados
@st.cache_data
def load_data():
    return pd.read_csv('data/vehicles.csv')

car_data = load_data()

# Cabeçalho principal
st.header('Dashboard de Análise de Vendas de Carros 🚗')

# Informações básicas sobre o dataset
st.subheader('Informações do Dataset')
st.write(f'Total de anúncios: {len(car_data)}')

# Seção de visualizações
st.subheader('Visualizações Interativas')

# Opção 1: Usando botões (versão básica)
st.write('**Versão com Botões:**')

col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Criar Histograma de Quilometragem')
    
    if hist_button:
        st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
        fig = px.histogram(car_data, x="odometer", 
                          title="Distribuição da Quilometragem dos Veículos",
                          labels={'odometer': 'Quilometragem', 'count': 'Quantidade'})
        st.plotly_chart(fig, use_container_width=True)

with col2:
    scatter_button = st.button('Criar Gráfico de Dispersão')
    
    if scatter_button:
        st.write('Criando um gráfico de dispersão para preço vs quilometragem')
        fig = px.scatter(car_data, x="odometer", y="price",
                        title="Relação entre Quilometragem e Preço",
                        labels={'odometer': 'Quilometragem', 'price': 'Preço ($)'})
        st.plotly_chart(fig, use_container_width=True)

# Divisor
st.divider()

# Opção 2: Usando checkboxes (versão avançada)
st.write('**Versão com Caixas de Seleção (Recomendada):**')

# Caixas de seleção
build_histogram = st.checkbox('Mostrar Histograma de Quilometragem')
build_scatter = st.checkbox('Mostrar Gráfico de Dispersão (Preço vs Quilometragem)')

# Histograma com checkbox
if build_histogram:
    st.write('Histograma da quilometragem dos veículos')
    fig_hist = px.histogram(car_data, x="odometer", 
                           title="Distribuição da Quilometragem dos Veículos",
                           labels={'odometer': 'Quilometragem (milhas)', 'count': 'Quantidade de Veículos'},
                           nbins=50)
    fig_hist.update_layout(showlegend=False)
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersão com checkbox
if build_scatter:
    st.write('Gráfico de dispersão: Preço vs Quilometragem')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                            title="Relação entre Quilometragem e Preço dos Veículos",
                            labels={'odometer': 'Quilometragem (milhas)', 'price': 'Preço ($)'},
                            opacity=0.6)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Rodapé
st.markdown("---")
st.write("Dashboard criado com Streamlit e Plotly Express")
