import time

from prefect import flow, task


@task(log_prints=True)
def my_task():
    import sys
    print(sys.version)


@flow(log_prints=True)
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
