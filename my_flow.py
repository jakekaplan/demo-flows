from prefect import flow
from datetime import datetime


@flow(log_prints=True)
def my_flow(datetime: datetime):
    print("It is currently:", datetime)


if __name__ == '__main__':
    flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="my-modal-deploy",
        work_pool_name="modal-pool-from-cli",
        enforce_parameter_schema=True
    )
