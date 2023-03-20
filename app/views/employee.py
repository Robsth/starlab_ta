import aiohttp_jinja2
from aiohttp import web
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db_connection import db_get_session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreateSchema, EmployeeUpdateSchema
from app.utils import serialize_employee


@aiohttp_jinja2.template("employee.html")
async def get_employees(request):
    async with db_get_session() as session:
        result = await session.execute(
            select(Employee).options(
                selectinload(Employee.supervisor),
                selectinload(Employee.subordinates),
            )
        )
        employees = result.scalars().all()
        serialized_employees = [serialize_employee(employee) for employee in employees]
    return {"employees": serialized_employees}


async def create_employee(request):
    try:
        data = await request.post()
        employee_data = EmployeeCreateSchema.parse_obj(data)
    except ValidationError as e:
        return web.HTTPBadRequest(reason=str(e.errors()))
    employee = Employee(**employee_data.dict())
    async with db_get_session() as session:
        session.add(employee)
        await session.commit()
    return web.HTTPFound("/employee")


async def edit_employee(request):
    employee_id = int(request.match_info["id"])

    try:
        data = await request.post()
        employee_data = EmployeeUpdateSchema.parse_obj({**data, "id": employee_id})
    except ValidationError as e:
        return web.HTTPBadRequest(reason=str(e.errors()))

    async with db_get_session() as session:
        employee = await session.get(Employee, employee_id)

        for field, value in employee_data.dict().items():
            setattr(employee, field, value)

        await session.commit()

    return web.HTTPFound("/employee")


async def delete_employee(request):
    data = await request.post()
    employee_id = int(data["employee_id"])

    async with db_get_session() as session:
        employee = await session.get(Employee, employee_id)
        await session.delete(employee)
        await session.commit()

    return web.HTTPFound("/employee")
