from prefect import flow
import os

@flow
def hello_world(a: str):
    print("hi!")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
