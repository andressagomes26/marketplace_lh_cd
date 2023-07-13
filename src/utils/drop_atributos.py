def drop_atrib(df):
    """Exclui as colunas id e veiculo_alienado do dataset
    Args:
        df (DataFrame): Dados;

    Returns:
        df: DataFrame após a exclusão das colunas;
    """

    df = df.drop('id', axis=1)
    df = df.drop('veiculo_alienado', axis=1)

    return df