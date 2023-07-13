import logging
import pandas as pd

from utils.read_dataset import read_dataset
from utils.missing_values import missing_values
from utils.drop_atributos import drop_atrib
from utils.normalizacao import normalizacao
from utils.one_hot import var_categoricas
from utils.one_hot import cat_unique
from utils.one_hot import atualiza_dataset
from utils.one_hot import union_cat
from utils.pca import pca_data

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

def pipeline_pre_processing(path_dataset_train, path_dataset_test):
    """Pipeline para o pré-processamento dos dados

    Args:
        path_dataset_train (String): Caminho do dataset de treinamento.
        path_dataset_test (String): Caminho do dataset de teste.
    """

    # Carregar
    try:
        logging.info(f'Carregando os datasets')
        df_train = read_dataset(path_dataset_train)
        df_teste = read_dataset(path_dataset_test)
    except:
        logging.error(f'O path indicado não existe')
        exit()

    # Valores Nulos
    logging.info(f'Realizando o tratamento dos dados nulos...')
    missing_values(df_train)
    missing_values(df_teste)

    id_df_teste = df_teste['id'].reset_index()
    
    # Drop atributos
    try:
        logging.info(f'Excluindo as colunas id e veiculo_alienado...')
        df_train = drop_atrib(df_train)
        df_teste = drop_atrib(df_teste)
    except:
        logging.error(f'O dataset não possui as colunas id ou veiculo_alienado')
        exit()

    # Codificação de Dados Categóricos
    logging.info(f'Realizando a codificação de Dados Categóricos...')
    var_categoricas(df_train)
    var_categoricas(df_teste)

    union_cat_train = cat_unique(df_train)
    union_cat_teste = cat_unique(df_teste)

    union_categories = union_cat(union_cat_train, union_cat_teste)

    atualiza_dataset(df_train, union_categories)
    atualiza_dataset(df_teste, union_categories)
    
    train_encoded = pd.get_dummies(df_train)
    test_encoded = pd.get_dummies(df_teste)

    # Normalizando os dados
    logging.info(f'Normalizando os dados...')
    normalizacao(train_encoded)
    normalizacao(test_encoded)

    # Separação da base de dados
    X = train_encoded.drop('preco', axis=1)
    y = train_encoded['preco']

    # PCA 
    logging.info(f'Realizando PCA...')
    X_pca_train = pca_data(X)
    X_pca_teste = pca_data(test_encoded)
    
    logging.info(f'Pré-processamento dos dados finalizado.')

    return X_pca_train, X_pca_teste, y, id_df_teste


