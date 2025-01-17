import time
import prefect
from prefect.runner.storage import GitRepository
from prefect import flow
from prefect.events.utilities import emit_event
from hashlib import md5


@flow(log_prints=True)
def demo_flow():
    print("Hi!")
    print(prefect.__version__)

if __name__ == "__main__":
    demo_flow.from_source(
        source=GitRepository(
            url="https://github.com/jakekaplan/demo-flows.git",
            branch="main",
        ),
        entrypoint="my_flow.py:demo_flow"
        ).deploy(
            name="event-test-deploy",
            work_pool_name="managed-pool"
        )

