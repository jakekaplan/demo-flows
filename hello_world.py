from prefect import flow
import os

@flow(log_prints=True)
def hello_world():
    for k, v in os.environ.items():
        print(k, v)
