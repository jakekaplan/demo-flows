from prefect import flow

@flow(log_prints=True)
def my_flow():
    x = []
    while True:
        x.append("a" * 1000000)

if __name__ == '__main__':
    my_flow()
