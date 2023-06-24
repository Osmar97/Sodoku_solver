import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import Perceptron

def read_data(file_path):
    """Lê os dados de um arquivo CSV e retorna os dados e rótulos."""
    data = pd.read_csv(file_path)
    data['spam'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)
    return data.Message, data.spam

def split_data(X, y):
    """Divide os dados em conjuntos de treinamento e teste."""
    return train_test_split(X, y)

def vectorize_text(X_train):
    """Converte o texto em vetores de contagem de tokens."""
    cv = CountVectorizer()
    X_train_counts = cv.fit_transform(X_train.values)
    return cv, X_train_counts

def train_naive_bayes(X_train_counts, y_train):
    """Treina um modelo MultinomialNB nos dados fornecidos."""
    model = MultinomialNB()
    model.fit(X_train_counts, y_train)
    return model

def train_perceptron(X_train_counts, y_train):
    """Treina um modelo Perceptron nos dados fornecidos."""
    model = Perceptron()
    model.fit(X_train_counts, y_train)
    return model

def evaluate_model(model, cv, X_test, y_test):
    """Avalia o desempenho do modelo nos dados de teste."""
    X_test_counts = cv.transform(X_test)
    return model.score(X_test_counts, y_test)

def train_and_evaluate(file_path):
    """Treina e avalia modelos MultinomialNB e Perceptron nos dados fornecidos."""
    # Ler os dados
    X, y = read_data(file_path)
    
    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Converter o texto em vetores de contagem de tokens
    cv, X_train_counts = vectorize_text(X_train)

    # Treinar o modelo MultinomialNB
    nb_model = train_naive_bayes(X_train_counts, y_train)

    # Treinar o modelo Perceptron
    perceptron_model = train_perceptron(X_train_counts, y_train)

    # Avaliar o desempenho dos modelos nos dados de teste
    nb_score = evaluate_model(nb_model, cv, X_test, y_test)
    perceptron_score = evaluate_model(perceptron_model, cv, X_test, y_test)

    return nb_score, perceptron_score

nb_score, perceptron_score = train_and_evaluate("spam.csv")
print(f"Naive Bayes score: {nb_score}")
print(f"Perceptron score: {perceptron_score}")
