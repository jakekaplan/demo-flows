from prefect import flow, Flow
import time

@flow(log_prints=True)
def my_flow():
    time.sleep(100000)


if __name__ == '__main__':
    my_flow()
    # flow.from_source(
    #     "https://github.com/jakekaplan/demo-flows.git",
    #     entrypoint="my_flow.py:my_flow"
    # ).deploy(name="jake-mex-deployment", work_pool_name="prefect-managed")
