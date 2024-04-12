import os
import mlflow

def train_model():
    model = ...
    mlflow.log_model(model, "model")
    mlflow.log_artifact("path/to/artifact")

if __name__ == 'main':
    models_folder = "models"
    if not os.path.exists(models_folder):
        os.makedirs(models_folder)

    with mlflow.start_run():
        mlflow.set_tag("team", "data-science")
        mlflow.set_tag("experiment", "experiment-1")
        train_model()

        model_path = os.path.join(models_folder, "my_model")
        mlflow.pyfunc.save_model(path=model_path, loader_module="mlflow.pyfunc")