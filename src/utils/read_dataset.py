import pandas as pd

def read_dataset(path):
    """Carrega o dataset. 

    Args:
        path (String): Caminho para o arquivo csv referente ao dataset.

    Returns:
        Dataframe: Dataframe.
    """

    df = pd.read_csv(path, sep=',')
    return df