def serialize_employee(employee, depth=0, max_depth=15):
    result = {
        "id": employee.id,
        "full_name": employee.full_name,
        "position": employee.position,
        "hire_date": employee.hire_date.isoformat(),
        "salary": employee.salary,
        "supervisor_id": employee.supervisor_id,
    }

    if depth < max_depth:
        result["subordinates"] = [
            serialize_employee(subordinate, depth + 1, max_depth)
            for subordinate in employee.subordinates
        ]
    else:
        result["subordinates"] = []

    return result
