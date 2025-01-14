import prefect
import os
from prefect import flow
from prefect.runner.storage import GitRepository


@flow(log_prints=True)
def demo_flow():
    print("hi!")
    print(os.environ)
    print(prefect.__version__)

if __name__ == "__main__":
    demo_flow.from_source(
        source=GitRepository(
            url="https://github.com/jakekaplan/demo-flows.git",
            branch="main",
        ),
        entrypoint="my_flow.py:demo_flow"
        ).deploy(
            name="coiled-deploy",
            work_pool_name="coiled-push"
        )

