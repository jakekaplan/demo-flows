import time

from prefect import flow
from prefect.runtime import flow_run
@flow(log_prints=True)
def my_flow():
    oom_maker = []
    while True:
        oom_maker.append('O'*1024**2)



if __name__ == '__main__':
    my_flow()
