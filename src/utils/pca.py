
from sklearn.decomposition import PCA

def pca_data(X):
    """Realiza a análise dos componentes principais. 

    Args:
        X (DataFrame): Dados;

    Returns:
        X_pca: Resultado após PCA;
    """
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    return X_pca