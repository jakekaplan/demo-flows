from prefect import flow
import time
from prefect.cli.deployment import run
@flow(log_prints=True)
def my_flow():
    print("I will sleep for 60 seconds.")
    time.sleep(60)
    print("I'm done!")


if __name__ == '__main__':
    my_flow()
