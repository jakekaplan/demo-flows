from prefect import flow, task, get_run_logger
from prefect.futures import wait
from prefect.runner.storage import GitRepository
import time

@task
def sleep(interval):
    time.sleep(interval)

def on_complete(flow, flow_run, state):
    logger = get_run_logger()
    logger.info("Done!!!")

def on_failure(flow, flow_run, state):
    logger = get_run_logger()
    logger.info("Failed!!!")

def on_crashed(flow, flow_run, state):
    logger = get_run_logger()
    logger.info("Crashed!!!")

@flow(on_completion=[on_complete], on_failure=[on_failure], on_crashed=[on_crashed])
def demo_flow(times, duration):
    futs = []
    for i in range(times):
        futs.append(sleep.submit(duration))

    wait(futs)

if __name__ == "__main__":
    demo_flow.from_source(
        source=GitRepository(
            url="https://github.com/jakekaplan/demo-flows.git",
            branch="main",
        ),
        entrypoint="my_flow.py:demo_flow"
        ).deploy(
            name="sleep-test",
            work_pool_name="managed-work-pool"
        )

