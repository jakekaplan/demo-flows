import time

from prefect import flow, task


@task
def my_task():
    time.sleep(15)

@flow
def my_flow():
    my_task()


if __name__ == '__main__':
    my_flow()
