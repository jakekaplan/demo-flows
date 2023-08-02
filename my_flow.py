from prefect import flow
import time


@flow(log_prints=True)
def my_flow(n: int = 15):
    print(f"I will sleep for {n} seconds.")
    time.sleep(n)
    print("I'm done!")


if __name__ == '__main__':
    my_flow()
