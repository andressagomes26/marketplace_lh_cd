from sklearn.preprocessing import MinMaxScaler

def normalizacao(df_encoded):
    """Realiza a normalização das variáveis numéricas

    Args:
        df (DataFrame): Dataframe

    Returns:
        None
    """
    norm = MinMaxScaler()

    colunas = ['num_fotos', 'ano_de_fabricacao', 'ano_modelo', 'hodometro', 'num_portas']

    for coluna in colunas:
        df_encoded[coluna] = norm.fit_transform(df_encoded[coluna].values.reshape(-1, 1))