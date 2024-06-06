import time
import prefect
import os
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print(prefect.__version__)
    print(os.environ)

if __name__ == "__main__":
    my_flow()