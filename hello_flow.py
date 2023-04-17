import sys
import prefect
from prefect import flow


@flow(log_prints=True)
def hi():
    print("Hi from Prefect! 🤗")
    print(f"Prefect Version: {prefect.__version__}")
    print(f"Python Version: {sys.version}")


if __name__ == "__main__":
    hi()
