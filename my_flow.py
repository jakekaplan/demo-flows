import os
import prefect
from prefect import flow, task

@task
def my_task():
    print(prefect.__version__)
    for k, v in os.environ.items():
        print(f"{k} : {v}")


@flow(log_prints=True)
def my_flow():
    print(prefect.__version__)
    my_task()



if __name__ == '__main__':
    my_flow()