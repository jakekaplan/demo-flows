import time
from prefect import flow
from prefect.runtime import flow_run


@flow(log_prints=True)
def my_flow():
    print(f"I'm in flow: {flow_run.name}. Sleeping for 5...")
    time.sleep(5)
    print("Done!")


if __name__ == '__main__':
    my_flow()

    # flow.from_source(
    #     "https://github.com/jakekaplan/demo-flows.git",
    #     entrypoint="my_flow.py:my_flow"
    # ).serve(
    #     name="jake-serve",
    #     interval=15
    # )

    # flow.from_source(
    #     "https://github.com/jakekaplan/demo-flows.git",
    #     entrypoint="my_flow.py:my_flow"
    # ).deploy(
    #     name="jake-mex-deployment",
    #     work_pool_name="prefect-managed"
    # )
