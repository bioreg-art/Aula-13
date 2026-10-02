import pandas as pd

df = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")


df_Id = df["salario"]

df_quantitativas = df[["salario", "lucro"]]

print(df_quantitativas)
