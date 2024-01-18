from prefect import flow, task
import marvin
import sys

@task
def get_version():
    return sys.version

@task
def print_version(version):
    print(version)


@flow(log_prints=True)
def my_flow():
    print("Hi from a flow!")
    version = get_version()
    print_version(version)
    print(marvin.__version__)


if __name__ == '__main__':
    flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="my-modal-deploy",
        work_pool_name="my-modal-pool",
    )
