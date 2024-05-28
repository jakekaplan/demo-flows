import time
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Starting flow")
    time.sleep(5)
    print("All done")


if __name__ == "__main__":
    my_flow()