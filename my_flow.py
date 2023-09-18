import time

from prefect import flow
from prefect.runtime import flow_run
from prefect_aws.workers.ecs_worker import ECSWorker



@flow(log_prints=True)
def my_flow():
    x = []
    while True:
        x.append(1)
    # print(f"Starting flow_run: {flow_run.name}")
    # time.sleep(15)
    # print(f"Finished flow_run: {flow_run.name}")


if __name__ == '__main__':
    my_flow()
