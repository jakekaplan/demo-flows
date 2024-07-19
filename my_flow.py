import prefect
from prefect import flow


@flow(log_prints=True)
def my_flow(payload: dict):
    print(type(payload))
    print(payload)


my_flow()