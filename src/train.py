import argparse
from pipeline_train import train_pipeline

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
                    help='Caminho para salvar o modelo treinado.')
    

    args = vars(ap.parse_args())

    train_pipeline(**args)



if __name__ == "__main__":
    main()
