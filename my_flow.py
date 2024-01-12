from prefect import flow, task
import sys

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
