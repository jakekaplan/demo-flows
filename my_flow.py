import pandas as pd
from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hello from a flow!")

    df = pd.DataFrame({"a": [1, 2, 3]})
    print(f"Here's a dataframe: {df}")


if __name__ == '__main__':
    my_flow()
