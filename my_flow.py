from prefect import flow


@flow
def my_flow():
    print(1)

if __name__ == '__main__':
    my_flow()
