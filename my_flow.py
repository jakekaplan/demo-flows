import time

from prefect import flow


@flow(log_prints=True)
def my_flow():
    time.sleep(1000)


if __name__ == '__main__':
    my_flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="my-modal-deploy",
        work_pool_name="my-modal-pool"
    )
