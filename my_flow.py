import time
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Sleeping for 1000s!")
    time.sleep(1000)
    print("Done sleeping!")
