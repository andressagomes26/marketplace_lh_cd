import argparse

def main():

    ap = argparse.ArgumentParser()

    
    ap.add_argument('-pm', '--path_model',
                    default= r'models/model_regressao_linear.pkl',
                    help='Caminho do modelo treinado.')

    args = vars(ap.parse_args())

if __name__ == "__main__":
    main()
