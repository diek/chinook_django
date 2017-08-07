from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Employee
# from .forms import EmployeeForm


def index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {
        'employees': employees,
    })


# def results(request, employee_id):
#     # employee = Employee.filter(id=employee_id)
#     response = "You're looking at the results of employee %s."
#     return HttpResponse(response % employee_id)


# def add_employee(request)
#     form = EmployeeForm(request.POST or None)
#     if form.is_valid():
#         form.save
