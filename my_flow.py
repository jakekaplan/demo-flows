from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hello world!")

my_flow.from_source(
    source="https://github.com/jakekaplan/demo-flows.git",
    entrypoint="my_flow.py:my_flow",
).deploy(
    name="my-managed-deployment",
    work_pool_name="my-managed-pool",
)