from prefect import flow
import flask

@flow(log_prints=True)
def my_flow():
    print("Hi from a flow")


# flow.from_source(
#     "https://github.com/jakekaplan/demo-flows.git",
#     entrypoint="my_flow.py:my_flow"
# ).deploy(
#     name="jake-pip-test",
#     work_pool_name="cloud-run-v2-push",
#     job_variables={
#         "env": {
#             "EXTRA_PIP_PACKAGES": "flask",
#         }
#     }
# )