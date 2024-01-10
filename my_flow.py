from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hi from a flow")
