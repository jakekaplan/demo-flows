from prefect import flow
import time

@flow
def my_flow():
    print("I will sleep for 10 seconds.")
    time.sleep(30)
    print("I'm done!")


if __name__ == '__main__':
    raise BaseException
    my_flow()
