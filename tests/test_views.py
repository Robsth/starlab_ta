import pytest
from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web
from datetime import date

from app.models.employee import Employee
from app.db_connection import db_get_session, db_init
from app.routes.employee import setup_employee_routes


@pytest.fixture(scope='function')
async def init_db():
    await db_init()


class TestEmployeeEndpoints(AioHTTPTestCase):
    async def get_application(self):
        app = web.Application()
        setup_employee_routes(app)
        return app

    async def setUpAsync(self):
        await db_init()
        async with db_get_session() as session:
            self.employee1 = Employee(full_name='John Doe', position='Manager', hire_date=date.today(), salary=50000)
            self.employee2 = Employee(full_name='Jane Smith', position='Developer', hire_date=date.today(), salary=40000)
            session.add_all([self.employee1, self.employee2])
            await session.commit()

    async def tearDownAsync(self):
        async with db_get_session() as session:
            await session.execute('DELETE FROM employee')
            await session.commit()

    async def test_get_employees(self, init_db):
        response = await self.client.get('/employee')
        assert response.status == 200
        employees = response.context['employees']
        assert len(employees) == 2

    async def test_create_employee(self, init_db):
        data = {'full_name': 'Test User', 'position': 'Tester', 'hire_date': '2023-01-01', 'salary': '35000'}
        response = await self.client.post('/employee/create', data=data)
        assert response.status == 302

        response = await self.client.get('/employee')
        assert response.status == 200
        employees = response.context['employees']
        assert len(employees) == 3
        assert any(employee['full_name'] == 'Test User' for employee in employees)

    async def test_edit_employee(self, init_db):
        data = {'full_name': 'Updated John Doe', 'position': 'Manager', 'hire_date': '2023-01-01', 'salary': '55000'}
        response = await self.client.post(f'/employee/edit/{self.employee1.id}', data=data)
        assert response.status == 302

        response = await self.client.get('/employee')
        assert response.status == 200
        employees = response.context['employees']
        assert any(employee['full_name'] == 'Updated John Doe' for employee in employees)

    async def test_delete_employee(self, init_db):
        data = {'employee_id': str(self.employee2.id)}
        response = await self.client.post('/employee/delete/{id}', data=data)
        assert response.status == 302

        response = await self.client.get('/employee')
        assert response.status == 200
        employees = response.context['employees']
        assert len(employees) == 1
        assert not any(employee['full_name'] == 'Jane Smith' for employee in employees)
