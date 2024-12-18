from prefect import flow, get_run_logger
from prefect.runner.storage import GitRepository
import time

@flow(log_prints=True)
async def demo_flow(date: str = None):
    logger = get_run_logger()
    logger.info(f"Sleeping forever...")
    time.sleep(10000)

if __name__ == "__main__":
    demo_flow.from_source(
        source=GitRepository(
            url="https://github.com/jakekaplan/demo-flow.git",
            branch="main"
            ),
        entrypoint="my_flow.py"
        ).deploy(
            name="modal-deployment",
            work_pool_name="my-modal-pool"
        )