import time
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Sleeping for 10s!")
    time.sleep(10)
    print("Done sleeping!")
