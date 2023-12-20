from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    #path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category/<int:pk>',views.category_detail, name='category-detail'),
    path('menu/', views.menu),
    #path('books/', views.BookList.as_view()),
    #path('books/<int:pk>', views.Book.as_view()),
]