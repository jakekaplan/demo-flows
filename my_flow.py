import time
from prefect import flow
import pandas as pd
from marvin import ai_fn


@ai_fn
def quote_marvin(topic: str) -> str:
    """Quote Marvin the robot from Hitchhiker's Guide on a topic"""


@flow(log_prints=True)
def my_flow():
    print("Hello world!")

    df = pd.DataFrame({'a': [1, 2, 3]})
    print(f"Here's a dataframe: {df}")

    quote = quote_marvin(topic="managed execution")
    print(f"Here's a quote {quote})")

    print("Goodbye world!")


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="my-managed-deployment",
        work_pool_name="my-managed-pool",
        job_variables={"pip_packages": ["pandas"]}
    )
