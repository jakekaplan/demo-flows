
from prefect import flow, task

@task
def my_task():
    import prefect
    print(prefect.__version__)

@flow(log_prints=True)
def my_flow():
    import prefect
    print(prefect.__version__)
    my_task()



if __name__ == '__main__':
    my_flow()