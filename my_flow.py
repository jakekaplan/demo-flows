from prefect import flow
from prefect.runner.storage import GitRepository


@flow(log_prints=True)
def demo_flow():
    print("hi!")

if __name__ == "__main__":
    demo_flow.from_source(
        source=GitRepository(
            url="https://github.com/jakekaplan/demo-flow.git",
            branch="main"
        ),
        entrypoint="my_flow.py"
        ).deploy(
            name="managed-deploy",
            work_pool_name="managed-pool"
        )