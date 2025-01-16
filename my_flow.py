import time
import prefect
from prefect.runner.storage import GitRepository
from prefect import flow
from prefect.events.utilities import emit_event


@flow(log_prints=True)
def demo_flow():
    print("running prefect: ", prefect.__version__)
    for i in range(1000):
        print(1)
        emit_event(
            event="external.resource.pinged",
            resource={"prefect.resource.id": "my.external.resource"}
        )
        time.sleep(1)


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

