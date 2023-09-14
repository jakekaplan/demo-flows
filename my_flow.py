import time

from prefect import flow
from prefect.runtime import flow_run


@flow(log_prints=True)
def my_flow():
    raise ValueError("Failed")

if __name__ == '__main__':
    my_flow()
