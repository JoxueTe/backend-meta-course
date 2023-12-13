from django.urls import path
from . import views
from .views import EmployeeCreate, EmployeeList, EmployeeDetail

urlpatterns = [
    path('about/', views.about),
    path('menu_card/', views.menu_by_id),
    path('home/', views.home),
    path('register/', views.register),
    path('login/', views.login),
    path('create/', EmployeeCreate.as_view(), name='EmployeeCreate'),
    path('list/', EmployeeList.as_view(), name='EmployeeList'),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
]