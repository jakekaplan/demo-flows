from prefect import flow, Flow
import pandas as pd

@flow(log_prints=True)
def my_flow():
    df = pd.DataFrame({"a": [1, 2, 3]})
    print(df)


if __name__ == '__main__':
    flow.from_source(
        "https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow"
    ).deploy(name="jake-mex-deployment", work_pool_name="prefect-managed")
