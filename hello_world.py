from prefect import flow
import os

@flow(log_prints=True)
def hello_world():
    print("hi!")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
