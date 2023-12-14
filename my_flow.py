import time
import pandera as pa
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hello world!")
    time.sleep(5)
    print("Goodbye world!")

if __name__ == '__main__':
    my_flow()