from prefect import flow, task
import marvin
import sys
import os

@task
def get_version():
    return sys.version

@task
def print_version(version):
    print(version)


@flow(log_prints=True)
def my_flow():
    v = get_version()
    print_version(v)
    print(marvin.__version__)
    print(os.environ["FOO"])

# flow.from_source(
#     source="https://github.com/jakekaplan/demo-flows.git",
#     entrypoint="my_flow.py:my_flow",
# ).deploy(
#     name="my-modal-deploy",
#     work_pool_name="my-modal-pool",
# )