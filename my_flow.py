import time
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Sleeping for 30s!")
    time.sleep(30)
    print("Done sleeping!")
