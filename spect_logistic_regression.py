#importando biblioteca
import pandas as pd

#importando conjunto de dados para treinamento
dataset_train = pd.read_csv('SPECT_train.txt')
X_train = dataset_train.iloc[:,1:].values
y_train = dataset_train.iloc[:,0].values

#importando conjunto de dados para teste do modelo
dataset_test = pd.read_csv('SPECT_test.txt')
X_test = dataset_test.iloc[:,1:].values
y_test = dataset_test.iloc[:,0].values

# treinando dados com modelo 'logistic regression'
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# criando variável dependente para previsão à partir das variáveis independentes de teste
y_pred = classifier.predict(X_test)

# criando 'confusion matrix' para ver quantos casos o modelo acertou e quantos errou
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print('número de acertos para diagnóstico normal (y=0): ', cm[0][0])
print('número de erros para diagnóstico normal (y=0): ', cm[0][1])
print('número de acertos para diagnóstico anormal (y=0): ', cm[1][1])
print('número de erros para diagnóstico anormal (y=0): ', cm[1][0])

# calculando precisão do modelo 'logistic regression' para o conjunto de dados
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
print('precisão: {:.2f}%'.format(accuracies.mean()*100))
print('desvio padrão: {:.2f}%'.format(accuracies.std()*100))
# precisão baixa e desvio padrão alto. 'logistic regression' não é o melhor modelo 
# para este conjunto de dados

