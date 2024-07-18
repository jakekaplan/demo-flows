import prefect
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print(prefect.__version__)


my_flow()