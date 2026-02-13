import pandas as pd
import ast

df = pd.read_csv("data/ticker_list.csv")
df['symbols'] = df['symbols'].apply(ast.literal_eval)

# 2. On récupère la valeur de 'yahoo' dans le premier dictionnaire (index 0)
df['symbol_Eurodex'] = df['symbols'].apply(lambda x: x[0]['yahoo'] if isinstance(x, list) and len(x) > 0 else None)
df['symbol_paris'] = df['symbol'] + ".PA"
df.to_csv('donnees_extraites.csv', index=False)