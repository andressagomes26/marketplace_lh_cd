import logging
from sklearn.linear_model import LinearRegression
import joblib
from pre_processing import pipeline_pre_processing

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

def train_pipeline(path_dataset_train, path_dataset_teste, path_model):
    """Pipeline para o treinamento do modelo

    Args:
        path_dataset_train (String): Caminho do dataset de treinamento.
        path_dataset_teste (String): Caminho do dataset de teste.
        path_model (String): Caminho para salvar o modelo.

    Returns:
        None
    """

    # Pré-processamento dos dados
    try:
        logging.info(f'Iniciando o pré-processamento dos dados')
        X_pca_train, _, y, _ = pipeline_pre_processing(path_dataset_train, path_dataset_teste)
    except:
        logging.error(f'Não foi possível realizar o pré-processamento dos dados')
        exit()


    # Treinamento
    logging.info(f'Iniciando o treinamento do modelo Regressão Linear...')
    model_regressao_linear = LinearRegression()
    model_regressao_linear.fit(X_pca_train, y)

    logging.info(f'Salvando o modelo treinado...')
    joblib.dump(model_regressao_linear, path_model)

    logging.info(f'Treinamento finalizado com sucesso.')