from prefect import flow
from pydantic import BaseModel
class SampleSize(BaseModel):
    total: int | None
    negative_class: int | None
    positive_class: int | None


class AnotherModel(BaseModel):
    sample_size: SampleSize

@flow
def sample_size_flow(param: AnotherModel):
    print(param)
    print(param.sample_size)


