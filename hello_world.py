import prefect
import fastapi
import starlette
from prefect import flow


@flow(log_prints=True)
def hello_world():
    print("prefect version: ", prefect.__version__)
    print("fastapi version: ", fastapi.__version__)
    print("starlette version: ", starlette.__version__)
