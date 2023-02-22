import sys
import prefect
from prefect import flow
import time


@flow(log_prints=True)
def hi():
    for i in range(30):
        print(f"{i}th minute...")
        time.sleep(60)


if __name__ == "__main__":
    hi()
