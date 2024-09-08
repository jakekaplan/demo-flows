import prefect
import fastapi
import starlette
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print(prefect.__version__)
    print(fastapi.__version__)
    print(starlette.__version__)


if __name__ == '__main__':
    my_flow()