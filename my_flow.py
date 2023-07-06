from prefect import flow
import time


@flow
def my_flow():
    time.sleep(30)


if __name__ == '__main__':
    my_flow()
