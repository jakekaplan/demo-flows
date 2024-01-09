from prefect import flow
import time


@flow(log_prints=True)
def my_flow():
    print("Hello from a flow!")

    time.sleep(15)
    print("Slept for 15 seconds")
