from datetime import date
from typing import Optional

from sqlalchemy.orm import declared_attr, relationship
from sqlmodel import Field, SQLModel


class Employee(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    full_name: str = Field(nullable=False)
    position: str = Field(nullable=False)
    hire_date: date = Field(nullable=False)
    salary: float = Field(nullable=False)

    supervisor_id: Optional[int] = Field(
        default=None, foreign_key="employee.id", nullable=True
    )

    @declared_attr
    def supervisor(cls):
        return relationship(
            "Employee", remote_side=[cls.id], back_populates="subordinates"
        )

    @declared_attr
    def subordinates(cls):
        return relationship(
            "Employee", remote_side=[cls.supervisor_id], back_populates="supervisor"
        )
