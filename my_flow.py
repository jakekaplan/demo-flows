from prefect import flow
from datetime import datetime


@flow(log_prints=True)
def my_flow(datetime: datetime):
    print("It is currently:", datetime)
