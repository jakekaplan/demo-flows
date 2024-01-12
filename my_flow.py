from prefect import flow
import sys

@flow(log_prints=True)
def my_flow():
    print(sys.version)
    print("Hello world!")

#
# flow.from_source(
#     "https://github.com/jakekaplan/demo-flows.git",
#     entrypoint="my_flow.py:my_flow"
# ).deploy(
#     name="modal-deploy",
#     work_pool_name="my-modal-pool"
# )
