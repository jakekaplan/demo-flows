from prefect import flow


@flow
def my_flow():
    print("Hello, world!")


if __name__ == '__main__':
    my_flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="my-modal-deploy",
        work_pool_name="modal-pool-from-cli"
    )
