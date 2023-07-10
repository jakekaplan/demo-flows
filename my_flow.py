from prefect import flow
import time

@flow
def my_flow():
    print("I will sleep for 60 seconds.")
    time.sleep(60)
    print("I'm done!")


if __name__ == '__main__':
    my_flow()
