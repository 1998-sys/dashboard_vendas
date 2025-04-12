import pandas as pd
import json

file = open('Dados/vendas.json')
data = json.load(file)

print(type(data))


df = pd.DataFrame.from_dict(data)
#print(df['Data da Compra'])

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

#print(df)

file.close()