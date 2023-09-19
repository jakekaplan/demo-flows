from prefect import task, flow
from prefect.deployments.deployments import Deployment
from prefect.task_runners import SequentialTaskRunner
from prefect.engine import orchestrate_task_run
import asyncio

@task(persist_result=True)
def task_1():
    print("success!")

@task(persist_result=True, cache_key_fn=lambda *args, **kwargs: "task_2")
def task_2():
    raise RuntimeError

@task(persist_result=True)
def task_3():
    print("success!")


@flow(task_runner=SequentialTaskRunner(), persist_result=True)
def demo_restart_issue():
    task_1()
    task_2()
    task_3()


if __name__ == "__main__":
    flow()