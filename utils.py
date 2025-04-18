from dataset import df
import pandas as pd
import streamlit as st
from time import sleep


def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix}{value:.2f} milhões'


df_rec_estado  = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# 2 - Dataframe receita mensal

df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))[['Preço']].sum().reset_index()

df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()


# 3 - Dataframe receita por categoria

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
#print(df_rec_categoria)

# 3 - Dataframe Vendedores (somatório e contagem de vendas)
df_vendedor = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count']))
print(df_vendedor)

# Função para converter arquivo CSV:
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso')
    sleep(3)
    success.empty()