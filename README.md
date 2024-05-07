# Gender-Recognition-MLOps

## basic pre-requisits
- Create template
- create setup.py
- create and install requirements
- create utility functions

## workflow
1. update config.yaml
2. update secrets.yaml [potional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src/config
6. update the components
7. update the pipeline
8. update main.py
9. update dvc.yaml

## DagsHub

```bash

save all the required credentials in environment variables
os.environ["MLFLOW_TRACKING_URI"] = ""
os.environ["MLFLOW_TRACKING_USERNAME"] = ""
os.environ["MLFLOW_TRACKING_PASSWORD"] = ""

or use export keyword

export MLFLOW_TRACKING_URI = your tracking uri
export MLFLOW_TRACKING_USERNAME = your tracking user name
export MLFLOW_TRACKING_PASSWORD = your tracking password

```

## DVC

First create the dvc.yaml file.

Then execute the following commands

```bash

dvc init # initialize dvc
dvc repro # to run dvc.yaml file
dvc dag # to see the pipeline visually on cmd

```