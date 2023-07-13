import pandas as pd
import logging
import joblib
from pre_processing import pipeline_pre_processing

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

def pipeline_test(path_dataset_train, path_dataset_teste, path_model, path_predicted):
    """Pipeline para salvar o resultado final do modelo

    Args:
        path_dataset_train (String): Caminho do dataset de treinamento.
        path_dataset_teste (String): Caminho do dataset de teste.
        path (String): Caminho do modelo.
        path_predicted (String): Caminho para salvar o arquivo com o resultado final do modelo.

    Returns:
        None
    """
    _, X_pca_teste, y, id_df_teste = pipeline_pre_processing(path_dataset_train, path_dataset_teste)


    logging.info(f'Realizando o carregamento do modelo treinado... ')
    model_regressao_linear = joblib.load(path_model)

    y_pred = model_regressao_linear.predict(X_pca_teste)

    df_predicted= pd.DataFrame()
    df_predicted['id'] = id_df_teste['id']
    df_predicted['predict'] = y_pred

    logging.info(f'Salvando arquivo com o resultado final do modelo... ')
    df_predicted.to_csv(path_predicted, index=False)
    
    logging.info(f'Arquivo salvo com sucesso em {path_predicted}')