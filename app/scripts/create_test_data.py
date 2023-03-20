import asyncio
from datetime import date

from app.db_connection import db_get_session
from app.models.employee import Employee


async def create_test_data():
    async with db_get_session() as async_session:
        async with async_session.begin():
            await async_session.execute(Employee.__table__.delete())
            employees = [
                Employee(
                    full_name="John Smith",
                    position="Manager",
                    hire_date=date(2020, 1, 1),
                    salary=100000.0,
                ),
                Employee(
                    full_name="Alice Johnson",
                    position="Assistant Manager",
                    hire_date=date(2020, 2, 1),
                    salary=80000.0,
                    supervisor_id=1,
                ),
                Employee(
                    full_name="Bob Brown",
                    position="Team Leader",
                    hire_date=date(2020, 3, 1),
                    salary=70000.0,
                    supervisor_id=2,
                ),
                Employee(
                    full_name="Charlie Davis",
                    position="Developer",
                    hire_date=date(2020, 4, 1),
                    salary=60000.0,
                    supervisor_id=3,
                ),
                Employee(
                    full_name="David Lee",
                    position="Developer",
                    hire_date=date(2020, 5, 1),
                    salary=60000.0,
                    supervisor_id=3,
                ),
                Employee(
                    full_name="Emma Martin",
                    position="Developer",
                    hire_date=date(2020, 6, 1),
                    salary=60000.0,
                    supervisor_id=4,
                ),
                Employee(
                    full_name="Frank Jackson",
                    position="Developer",
                    hire_date=date(2020, 7, 1),
                    salary=60000.0,
                    supervisor_id=4,
                ),
                Employee(
                    full_name="George Baker",
                    position="Developer",
                    hire_date=date(2020, 8, 1),
                    salary=60000.0,
                    supervisor_id=5,
                ),
                Employee(
                    full_name="Hannah Wilson",
                    position="Developer",
                    hire_date=date(2020, 9, 1),
                    salary=60000.0,
                    supervisor_id=5,
                ),
                Employee(
                    full_name="Isabella Taylor",
                    position="Developer",
                    hire_date=date(2020, 10, 1),
                    salary=60000.0,
                    supervisor_id=5,
                ),
            ]
            async_session.add_all(employees)
            await async_session.commit()


if __name__ == "__main__":
    asyncio.run(create_test_data())
