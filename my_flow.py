from time import sleep
from prefect import flow

@flow(log_prints=True, job_variables={"image": "asdkjfnaksjdfnaksdjfnaksjdfn"})
def my_flow():
    print("hello world!")