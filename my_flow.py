import os
import prefect
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("hello world!")
    for k, v in os.environ.items():
        print(f"{k}={v}")

