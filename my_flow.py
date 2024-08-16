import prefect
from prefect import flow


@flow
def my_flow():
    print("Hello, world!")
    print(prefect.__version__)
