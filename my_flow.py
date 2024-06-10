from prefect import flow


@flow
def cute_flow(might_delete_later: str = 123):
    print("I'm a cute flow!")
