from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

app = FastAPI()

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class KNNRequest(BaseModel):
    k: int
    sample: list

class KMeansRequest(BaseModel):
    k: int

@app.get("/")
def root():
    return {"message": "Welcome to the Iris Dataset API! Use /knn or /kmeans endpoints."}

@app.post("/knn/")
def knn_predict(request: KNNRequest):
    try:
        if not (1 <= request.k <= len(X_train)):
            raise ValueError(f"k must be between 1 and {len(X_train)}")
        
        model = KNeighborsClassifier(n_neighbors=request.k)
        model.fit(X_train, y_train)
        prediction = model.predict([request.sample])

        accuracy = accuracy_score(y_test, model.predict(X_test))
        return {
            "sample": request.sample,
            "predicted_class": iris.target_names[prediction[0]],
            "model_accuracy": accuracy,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/kmeans/")
def kmeans_predict(request: KMeansRequest):
    try:
        if request.k < 1:
            raise ValueError("k must be greater than 0")
        
        model = KMeans(n_clusters=request.k, random_state=42)
        model.fit(X)

        cluster_centers = model.cluster_centers_.tolist()
        labels = model.labels_.tolist()

        return {
            "k": request.k,
            "cluster_centers": cluster_centers,
            "labels": labels,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
