

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Employee

def employee_details(request):
    employees = Employee.objects.all()
    selected_employee = None
    if 'employee_id' in request.GET:
        selected_employee = get_object_or_404(Employee, employee_id=request.GET['employee_id'])
    
    
    if selected_employee:
        age = now().year - selected_employee.date_of_birth.year - ((now().month, now().day) < (selected_employee.date_of_birth.month, selected_employee.date_of_birth.day))
    else:
        age = None

    return render(request, 'management_tool/employee_details.html', {
        'employees': employees,
        'selected_employee': selected_employee,
        'age': age,
    })


