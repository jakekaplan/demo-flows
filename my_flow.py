import sys
import time

from prefect import flow, task
from prefect.runtime import flow_run
from prefect.runtime import deployment
from prefect.client.orchestration import get_client

@task
def my_task():
    time.sleep(99999)
    # raise ValueError("This is a test")


@flow
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
