from prefect import flow
from prefect.deployments import run_deployment
import time


@flow(log_prints=True)
def my_flow():
    print("Hello from a flow!")

    for i in range(20):
        time.sleep(10)
        print("Slept for 10 seconds")
