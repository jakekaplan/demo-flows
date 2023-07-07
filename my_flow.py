from prefect import flow
import time

@flow
def my_flow():
    print("I will sleep for ever... seconds.")
    time.sleep(10000000)
    print("I'm done!")


if __name__ == '__main__':
    my_flow()
