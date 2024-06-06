import time
import prefect
import os
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print(prefect.__version__)
    print(os.environ)
    print("sleeping for 30s")
    time.sleep(30)

if __name__ == "__main__":
    my_flow()