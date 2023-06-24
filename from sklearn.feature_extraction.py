from sklearn.feature_extraction.text import CountVectorizer

# Dados de texto
corpus = [
    'Este é o primeiro documento.',
    'Este é o segundo documento.',
    'E este é o terceiro documento.',
]

# Inicializar CountVectorizer
vectorizer = CountVectorizer()

# Ajustar e transformar os dados
X = vectorizer.fit_transform(corpus)

# Imprimir a matriz resultante
print(X.toarray())
