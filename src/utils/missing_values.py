import statistics as sts
import numpy as np

def missing_values(df):
    """Realiza o tratamento dos valores missing no DataFrame

    Args:
        df (DataFrame): Dataframe para tratamento (df_train / df_teste)

    Returns:
        None
    """

    colunas = ['dono_aceita_troca', 'veiculo_único_dono', 'revisoes_concessionaria', 'ipva_pago', 'veiculo_licenciado', 'garantia_de_fábrica', 'revisoes_dentro_agenda']
    values = ['Nao aceita troca', 'Não é único dono', 'Não possui todas as revisoes feitas pela concessionaria', 'ipva não pago', 'Não Licenciado', 'Não possui garantia de fábrica', 'não possui todas as revisões feitas pela agenda do carro']

    for i, coluna in enumerate(colunas):
        df[coluna] = df[coluna].replace(np.nan, values[i])

    df['num_fotos'].fillna(sts.median(df['num_fotos']), inplace=True)
