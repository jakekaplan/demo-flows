import time

from prefect import flow
from prefect.runtime import flow_run
from prefect_gcp.worker import CloudRunWorker

@flow(log_prints=True)
def my_flow():
    print(f"Starting flow run: {flow_run.name}")
    time.sleep(10)
    print(f"Finishing flow run: {flow_run.name}")


if __name__ == '__main__':
    my_flow()
