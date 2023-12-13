from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Menu, Employee


def home(request):
    return render(request, "home.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})

def about(request):
    about_content = {'about': "This is about a site the i dont want to create context for, or design."}
    return render(request, "about.html", about_content)

# def menu(request):
#     menu_item = {'menu': [
#         {'name':"arepa", 'price':"12"},
#         {'name':"cachapa", 'price':"15"},
#         {'name':"empanada", 'price':"10"},
#         {'name':"tequeño", 'price':"10"},
#     ]}
#     return render(request, 'menu.html', menu_item)

def menu_by_id(request):
    new_menu = Menu.objects.all()
    menu_dic = {'menu': new_menu}
    return render(request, 'menu_card.html', menu_dic)


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = "/employees/success/"


class EmployeeList(ListView):
    model = Employee
    success_url = "/employees/success"

class EmployeeDetail(ListView):
    model = Employee
    success_url = "/employees/success"