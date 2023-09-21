import time

from prefect import flow
from prefect.runtime import flow_run
@flow(log_prints=True)
def my_flow():
    x = []
    while True:
        x.append("aaaaaaa" * 100000000)
    # print(f"Starting flow run: {flow_run.name}")
    # time.sleep(10)
    # print(f"Finishing flow run: {flow_run.name}")


if __name__ == '__main__':
    my_flow()
