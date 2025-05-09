import pandas as pd

# Carregando o conjunto de dados
df = pd.read_csv('dirty_cafe_sales.csv')

# Conhecendo os dados
df.head(10)
df.columns
df.shape

# Verificando a existência de dados nulos
df.isnull().sum()

# Substituindo valores problemáticos por NaN
df.replace(['UNKNOWN', 'ERROR', ' ', ''], pd.NA, inplace=True)

# Removendo linhas com NaNs em colunas críticas
df.dropna(inplace=True)

# Removendo duplicatas
df.drop_duplicates(inplace=True)

# Alterando os dtypes
df.dtypes
df['Quantity'] = df['Quantity'].astype(int)
df['Price Per Unit'] = df['Price Per Unit'].astype(float)
df['Total Spent'] = df['Total Spent'].astype(float)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
df['Payment Method'] = df['Payment Method'].astype('category')
df['Location'] = df['Location'].astype('category')

# Tratando valores ausentes após conversão
df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent', 'Transaction Date'], inplace=True)

# Corrigindo Total Spent com base em Quantity * Price Per Unit
df['Expected Total'] = df['Quantity'] * df['Price Per Unit']
df['Total Spent'] = df['Expected Total']
df.drop(columns='Expected Total', inplace=True)

# Padronizando textos categóricos
df['Payment Method'] = df['Payment Method'].str.strip().str.title().astype('category')
df['Location'] = df['Location'].str.strip().str.title().astype('category')

# Verificando resultado
df.info()
df.describe(include='all')
