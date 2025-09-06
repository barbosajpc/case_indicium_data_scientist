# Projeto de Previsão de `IMDB_Rating`

Este projeto tem como objetivo prever o `IMDB_Rating` de filmes utilizando técnicas de **Machine Learning** e dados obtidos do IMDb e OMDB. O fluxo de trabalho inclui etapas de Análise Exploratória de Dados (EDA), **Feature Engineering**, treinamento, otimização e avaliação de modelos de regressão.

---

## Estrutura do Projeto

A organização do projeto segue a seguinte estrutura de diretórios, garantindo clareza e separação das etapas:

```
.
├── data/
│   ├── predicted/
│   │   └── imdb_rating_pred.csv
│   ├── processed/
│   │   ├── dados_omdb.csv
│   │   └── data_cleaned.csv
│   ├── raw/
│   │   └── desafio_indicium_imdb.csv
│   ├── test/
│   │   └── data_test_model.csv
│   └── train/
│       └── data_train_model.csv
├── models/
│   └── RandomForest.pkl
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_modeling.ipynb
├── src/
│   └── eda_utils.py
├── .env
├── .env_exemplo
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Instalação e Execução

Para instalar e executar o projeto, siga os passos abaixo:

### 1. Clonar o Repositório

Primeiro, clone o repositório para a sua máquina local:

```bash
git clone git@github.com:barbosajpc/case_indicium_data_scientist.git
cd case_indicium_data_scientist
```

### 2. Configurar o Ambiente

É altamente recomendado criar um ambiente virtual para gerenciar as dependências do projeto.

```bash
# Criar o ambiente virtual (Python 3.x)
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS e Linux:
source venv/bin/activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar os Notebooks

O fluxo de trabalho completo do projeto está contido nos dois Jupyter Notebooks localizados na pasta `notebooks/`:

- **`01_EDA.ipynb`**: Contém a Análise Exploratória de Dadose  a limpeza inicial.
- **`02_modeling.ipynb`**: Contém o Feature Engineering, treinamento dos modelos de Machine Learning, a otimização de hiperparâmetros com Optuna e a avaliação final.

Para executá-los, inicie o Jupyter Notebook ou JupyterLab no diretório raiz do projeto:

```bash
jupyter notebook
```

Navegue até a pasta `notebooks` e execute as células de cada arquivo na ordem correta para reproduzir o projeto.