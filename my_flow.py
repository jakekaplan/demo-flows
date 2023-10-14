import time

from prefect import flow, task


@task
def my_task():
    import sys
    print(sys.version)


@flow
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
