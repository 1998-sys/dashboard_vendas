import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedor

grafic_map_estado = px.scatter_geo(   
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size = 'Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data= {'lat': False, 'lon': False},
    title = 'Receita por Estado')


grafic_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    color = 'Ano',
    line_dash='Ano',
    title='Receita Mensal'
)

grafic_rec_mensal.update_layout(yaxis_title='Receita (R$)')


grafic_rec_estado = px.bar(
    df_rec_estado.head(7),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top Receita por Estado'
)


grafic_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto=True,
    title='Top 7 Categorias com Maior Receita'
)


grafic_rec_vendedor = px.bar(
    df_vendedor[['sum']].sort_values('sum', ascending=False).head(7),
    x='sum',
    y=df_vendedor[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 Vendedores por Receita'
)

grafic_rec_vendedor.update_layout(yaxis_title='Vendedor')
grafic_rec_vendedor.update_layout(xaxis_title='Receita Gerada (R$)')

grafic_qtd_vendas_vendedor = px.bar(
    df_vendedor[['count']].sort_values('count', ascending=False).head(7),
    x = df_vendedor[['count']].sort_values('count', ascending=False).head(7).index,
    y = 'count',
    text_auto=True,
    title='Top 7 Vendendores por Quantidade de Vendas'
)

grafic_qtd_vendas_vendedor.update_layout(yaxis_title='Unidades Vendidas')
grafic_qtd_vendas_vendedor.update_layout(xaxis_title='Vendedor')