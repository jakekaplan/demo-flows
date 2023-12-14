import time
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hello world!")
    for i in range(60):
        print(f"{i}th minute, sleeping for 60 seconds...")
        time.sleep(60)
    print("Goodbye world!")


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="mex-deployment",
        work_pool_name="mex-work-pool",
    )
