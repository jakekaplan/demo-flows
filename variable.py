import os
from prefect import flow


@flow(log_prints=True)
def variable_flow(my_var):
    print(my_var)
    print(type(my_var))


@flow(log_prints=True)
def my_env_var_flow():
    print(os.environ.get("MY_ENV_VAR"))
    print(os.environ.get("MY_OTHER_ENV_VAR"))


if __name__ == '__main__':
    variable_flow.serve()
