from prefect import flow
import time


@flow(log_prints=True)
def my_flow(n: int = 15):
    import sys
    print(sys.executable)


if __name__ == '__main__':
    my_flow()
