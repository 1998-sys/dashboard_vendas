import streamlit as st
import plotly.express as px
from dataset import df
import utils
from grafico import grafic_map_estado, grafic_rec_mensal, grafic_rec_estado, grafic_rec_categoria, grafic_rec_vendedor, grafic_rec_vendedor, grafic_qtd_vendas_vendedor



st.set_page_config(layout='wide')
st.title('Dashboard de Vendas :shopping_trolley:')

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
  )

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2, aba3 = st.tabs(['Datasets', 'Receita', 'Vendedores']) # Criando abas

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', utils.format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafic_map_estado, use_container_width=True)
        st.plotly_chart(grafic_rec_estado, use_container_width=True)
        
        
    
    with coluna2:
        st.metric('Quantidade Vendas', utils.format_number(df.shape[0]))
        st.plotly_chart(grafic_rec_mensal, use_container_width=True)
        st.plotly_chart(grafic_rec_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafic_rec_vendedor, use_container_width=True)
    with coluna2:
        st.plotly_chart(grafic_qtd_vendas_vendedor, use_container_width=True)

