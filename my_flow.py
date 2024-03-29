from prefect import flow


@flow(log_prints=True)
def my_flow():
    print("Hello, world!")


if __name__ == '__main__':
    my_flow.from_source(
        source="https://github.com/jakekaplan/demo-flows.git",
        entrypoint="my_flow.py:my_flow",
    ).deploy(
        name="aws-push-deploy",
        work_pool_name="ecs-push-pool"
    )
