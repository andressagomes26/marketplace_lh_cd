# <h1 align="center"><font color = #119fbf>Previsão de preços de veículos | Cientista de Dados 🌎🚀</font></h1>
Nesse projeto é realizada a análise exploratória dos dados (EDA) de um marketplace de compra e venda de veículos usados, a fim de responder às perguntas de negócios. E em seguida, serão utilizados modelos preditivos de Machine Learning para precificar os carros do cliente. 

# Arquivos
Lista de arquivos utilizados neste projeto:
- Dataset de treinamento: *./dataset/cars_train.csv*
- Dataset de teste: *./dataset/cars_test.csv*
- Notebook EDA: *./notebooks/EDA.ipynb*
- Notebook modelagem: *./notebooks/modelagem_regressao.ipynb*
- Modelo Treinado: *./models/model_regressao_linear.pkl*
- Resultado do modelo: *./results/predicted.csv*
- Códigos de modelagem: *./src/*
- Link GitHub: *https://github.com/andressagomes26/marketplace_lh_cd.git*

# Instalar e executar o projeto

Para utilizar este projeto deve-se clonar o repositório do github e executar o seguinte comando dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

Para treinar o modelo de regressão linear pode-se executar o comando abaixo:

```bash
python src/train.py
```

Caso seja necessário alterar o caminho da pasta do dataset ou o caminho em que o modelo será salvo, pode-se enviar estes caminhos como argumento. Sendo eles:

```bash
--path_dataset_train <caminho_dataset_treinamento> 
--path_dataset_teste <caminho_dataset_teste> 
--path_model <caminho_modelo>
```

Para testar o modelo de regressão linear e salvar o arquivo ‘predicted.csv’ com o resultado do modelo pode-se executar o comando abaixo:
```bash
python src/test.py
```

Caso seja necessário alterar o caminho da pasta do dataset, o caminho em que os modelos serão salvos, ou o caminho para salvar o arquivo predicted.csv, pode-se enviar estes caminhos como argumento. Sendo eles:
```bash
--path_dataset_train <caminho_dataset_treinamento> 
--path_dataset_teste <caminho_dataset_teste> 
--path_model <caminho_modelo>
--path_predicted <caminho_predicted>
```
