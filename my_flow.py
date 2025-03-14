
from prefect import flow

@flow(log_prints=True)
def my_flow():
    x = []
    while True:
        x.append("sdkjfnasjkdfnkadsjf" * 100000)
