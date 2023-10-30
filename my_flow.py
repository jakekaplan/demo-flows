import time

from prefect import flow, task
import os

@flow(log_prints=True)
def my_flow():
    test1 = os.getenv("TEST1", "test1 not set")
    print(test1)
    test2 = os.getenv("TEST2", "test2 not set")
    print(test2)


if __name__ == '__main__':
    my_flow()
