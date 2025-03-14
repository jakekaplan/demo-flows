from time import sleep
from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("SLEEPING FOREVER!!!")
    while True:
        sleep(1)
