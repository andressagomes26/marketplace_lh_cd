import argparse
from pipeline_train import train_pipeline

def main():

    ap = argparse.ArgumentParser()

    ap.add_argument('-pd', '--path_dataset',
                    default=r"dataset/cars_train.csv",
                    help='Caminho do conjunto de dados de treinamento.')
    
    ap.add_argument('-pm', '--path_model',
                    default= r'models/regressao_new.pkl',
                    help='Caminho para salvar o modelo treinado.')
    

    args = vars(ap.parse_args())

    train_pipeline(**args)



if __name__ == "__main__":
    main()
