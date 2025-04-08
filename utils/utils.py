import pandas as pd

def carregar_dados(caminho_arquivo):
    """Carrega dados de um arquivo CSV."""
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"Dados carregados com sucesso de: {caminho_arquivo}")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em: {caminho_arquivo}")
        return None

def checar_dados_iniciais(df):
    """Realiza uma checagem inicial da qualidade dos dados."""
    print("\n--- Checagem Inicial dos Dados ---")
    print(f"Número de linhas: {len(df)}")
    print(f"Número de colunas: {df.shape[1]}")
    print("\nTipos de dados das colunas:")
    print(df.dtypes)
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())
    print("\nPrimeiras 5 linhas:")
    print(df.head())