from prefect import task, flow

@task()
def task1():
    print("trying task 1")

@task()
def task2():
    print("trying task 2")
    raise ValueError("fail")


@flow(retries=2, log_prints=True)
def run_tasks():
    task1()
    task2()

if __name__ == "__main__":
    run_tasks()