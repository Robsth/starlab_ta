from aiohttp import web

from app.views.employee import (create_employee, delete_employee,
                                edit_employee, get_employees)


def setup_employee_routes(app):
    app.router.add_get("/employee", get_employees)
    app.router.add_route("POST", "/employee/create", create_employee)
    app.router.add_route("POST", "/employee/edit/{id}", edit_employee)
    app.router.add_route("POST", "/employee/delete/{id}", delete_employee)

    @web.middleware
    async def handle_404(request, handler):
        try:
            return await handler(request)
        except web.HTTPNotFound:
            return web.Response(text="404 Not Found", status=404)

    app.middlewares.append(handle_404)
