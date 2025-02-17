import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 📌 Cargar datos de ejemplo (Dataset de flores Iris)
iris = load_iris()
X, y = iris.data, iris.target

# 📌 Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📌 Crear y entrenar el modelo de Regresión Logística
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 📌 Guardar el modelo en un archivo .pkl
joblib.dump(model, "modelo_entrenado.pkl")

print("✅ Modelo guardado como 'modelo_entrenado.pkl'")


# Clase	Sepal Length	Sepal Width	Petal Length	Petal Width
# Setosa (0)	5.0 - 5.8 cm	3.2 - 4.4 cm	1.0 - 1.9 cm	0.1 - 0.6 cm
# Versicolor (1)	5.5 - 6.3 cm	2.3 - 3.4 cm	3.0 - 5.1 cm	1.0 - 1.8 cm
# Virginica (2)	6.3 - 7.9 cm	2.5 - 3.8 cm	4.5 - 6.9 cm	1.4 - 2.5 cm