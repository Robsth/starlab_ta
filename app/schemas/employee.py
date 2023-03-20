from datetime import date
from typing import Optional, Union

from pydantic import BaseModel, PositiveFloat, PositiveInt, constr, validator


class EmployeeCreateSchema(BaseModel):
    full_name: constr(min_length=3, max_length=100)
    position: constr(min_length=2, max_length=100)
    hire_date: date
    salary: PositiveFloat
    supervisor_id: Optional[Union[PositiveInt, str]]

    @validator("supervisor_id", pre=True)
    def str_to_int_or_none(cls, value):
        if value == "":
            return None
        if isinstance(value, str) and value.isnumeric():
            return int(value)
        return value


class EmployeeUpdateSchema(EmployeeCreateSchema):
    id: PositiveInt
