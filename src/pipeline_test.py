import pandas as pd
from sklearn.model_selection import train_test_split
from dataset.utils import read_pre_processing_dataset
from text.utils import lemmatize
from models.vectorizer import vetorizer_tfidf
from sklearn.linear_model import LogisticRegression
from models.classifiers import train_models, logistic_regression
from models.io_models import save_model
import logging
from models.io_models import load_model

def predict_pipeline(text, path_model,path_count,path_tfidf):
    """Pipeline para predição do sentimento de um texto

    Args:
        text (String): Texto que o sentimento deve ser analisado.
        path_model (Sklearn Model): Caminho do classificador treinado.
        path_count (CountVectorizer): Caminho do CountVectorizer salvo.
        path_tfidf (TfidfTransformer): Caminho do tf-idf salvo.

    Returns:
        Int: Predição do sentimento do texto
                0 - Sentimento Ruim
                1 - Sentimento Bom
    """
    text_lemma = lemmatize(text)

    try:
        logging.info(f'Realizando predição do texto: {text}')
        vetorizer  = load_model(path_count)
        text_vec = vetorizer.transform([' '.join(text_lemma)])

        transformer  = load_model(path_tfidf)
        text_vec = transformer.transform(text_vec)

        model  = load_model(path_model)
        pred = model.predict(text_vec)   

        if(pred[0]==0):     
            logging.info(f'O Sentimento é ruim.')
        else:
            logging.info(f'O Sentimento é bom.')
    except:
        logging.error(f'Algum path pode não existir.')
        exit()

    return pred[0]