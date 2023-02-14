import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Application de prédiction simple de fleur d'Iris

Cette application prédit le **type de fleur** d'Iris!
""")

st.sidebar.header('Les paramètres d\'entrée de l\'utilisateur.')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Les paramètres d\'entrée de l\'utilisateur.')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Les étiquettes de classe et leur numéro d\'index correspondant.')
st.write(iris.target_names)

st.subheader('Prédiction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Probabilité de prédiction.')
st.write(prediction_proba)
