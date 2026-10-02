import pandas as pd

df = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")

df_qualitativas = df[["id", "nome", "departamento", "ativo", "data de nascimento"]]





print(df_qualitativas)



