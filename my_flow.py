from time import sleep
from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("sleeping forever!!!")
    sleep(99999999999999)
