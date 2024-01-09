from prefect import flow, task

@task
def my_task(n):
    return n + 1


@flow
def my_subflow():
    nums = [i for i in range(1000)]
    my_task.map(nums)
