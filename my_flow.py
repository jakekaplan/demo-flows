import prefect
from prefect import flow
from pydantic import BaseModel


class MyModel(BaseModel):
    x: int
    y: str


@flow
def my_flow(my_model: MyModel):
    print(type(my_model))
    print(my_model)
    print(prefect.__version__)
