from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("HELLO!!!")


if __name__ == '__main__':
    my_flow()