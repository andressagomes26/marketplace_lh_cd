import argparse
from pipeline_test import pipeline_test

def main():

    ap = argparse.ArgumentParser()

    ap.add_argument('-pt', '--path_dataset_train',
                    default=r"dataset/cars_train.csv",
                    help='Caminho do conjunto de dados de treinamento.')
    
    ap.add_argument('-pd', '--path_dataset_teste',
                    default=r"dataset/cars_test.csv",
                    help='Caminho do conjunto de dados de teste.')
    
    ap.add_argument('-pm', '--path_model',
                    default= r'models/model_regressao_linear.pkl',
                    help='Caminho do modelo treinado.')
    
    ap.add_argument('-pr', '--path_predicted',
                    default= r'results/predicted.csv',
                    help='Caminho para salvar o arquivo com o resultado do modelo treinado.')
    

    args = vars(ap.parse_args())

    pipeline_test(**args)


if __name__ == "__main__":
    main()
