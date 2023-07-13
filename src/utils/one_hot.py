import pandas as pd

def var_categoricas(df):
    """Realiza a codificação das variáveis categóricas binárias

    Args:
        df (DataFrame): Dataframe para tratamento (df_train / df_teste)

    Returns:
        None
    """

    df['entrega_delivery'].replace([True,  False],[0,1],inplace=True)
    df['troca'].replace([True,  False],[0,1],inplace=True)
    df['elegivel_revisao'].replace([True,  False],[0,1],inplace=True)
    df['blindado'].replace(['N','S'],[0,1],inplace=True)
    df['tipo_vendedor'].replace(['PF', 'PJ'],[0,1],inplace=True)
    df['dono_aceita_troca'].replace(['Aceita troca', 'Nao aceita troca'],[0,1],inplace=True)
    df['veiculo_único_dono'].replace(['Único dono', 'Não é único dono'],[0,1],inplace=True)
    df['revisoes_concessionaria'].replace(['Todas as revisões feitas pela concessionária', 'Não possui todas as revisoes feitas pela concessionaria'],[0,1],inplace=True)
    df['ipva_pago'].replace(['IPVA pago', 'ipva não pago'],[0,1],inplace=True)
    df['veiculo_licenciado'].replace(['Licenciado', 'Não Licenciado'],[0,1],inplace=True)
    df['garantia_de_fábrica'].replace(['Garantia de fábrica', 'Não possui garantia de fábrica'],[0,1],inplace=True)
    df['revisoes_dentro_agenda'].replace(['Todas as revisões feitas pela agenda do carro', 'não possui todas as revisões feitas pela agenda do carro'],[0,1],inplace=True)

def cat_unique(df):
    """Adiciona os valores únicos do DataFrame em um array

    Args:
        df (DataFrame): Dataframe

    Returns:
        val_unique (array): Valores únicos do DataFrame
    """

    colunas = ['marca', 'modelo', 'versao', 'tipo', 'cor', 'cidade_vendedor', 'estado_vendedor', 'cambio', 'anunciante']
    val_unique = []

    for coluna in colunas:
        val_unique.append(set(df[coluna].unique()))

    return val_unique

def union_cat(union_cat_train, union_cat_teste):
    """Realiza uma operação de união entre os valores únicos do DataFrame de treinamento e de teste.

    Args:
        union_cat_train (array): Valores únicos do DataFrame de treinamento (df_train)
        union_cat_teste (array): Valores únicos do DataFrame de teste (df_teste)

    Returns:
        union_cat_resultado (array): Array com os valores únicos do DataFrame de treinamento e de teste.
    """
    colunas = ['marca', 'modelo', 'versao', 'tipo', 'cor', 'cidade_vendedor', 'estado_vendedor', 'cambio', 'anunciante']
    union_cat_resultado = []

    for i, coluna in enumerate(colunas):
        union_cat_resultado.append(union_cat_train[i].union(union_cat_teste[i]))

    return union_cat_resultado

def atualiza_dataset(df, union_categories):
    """ Atualiza os DataFrames com as categorias unificadas

    Args:
        df (DataFrame): Dataframe (df_train ou df_teste)
        union_cat_resultado (array): Valores únicos do DataFrame de treinamento e de teste.

    Returns:
        None
    """

    colunas = ['marca', 'modelo', 'versao', 'tipo', 'cor', 'cidade_vendedor', 'estado_vendedor', 'cambio', 'anunciante']

    for i, coluna in enumerate(colunas):
        df[coluna] = df[coluna].astype('category').cat.set_categories(union_categories[i])