from prefect import flow


@flow(log_prints=True)
def my_flow(event):
    print(type(event))
    print(event)


if __name__ == '__main__':
    my_flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="hydration-demo",
        work_pool_name="modal-pool-from-cli"
    )
