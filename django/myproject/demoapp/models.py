from django.db import models

# Create your models here.


class MenuCategory(models.Model):
    menu_Category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.menu_Category_name

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None,related_name="category_name")

    def __str__(self) -> str:
        return self.menu_item


# class Logger(models.Model): 
#     first_name = models.CharField(max_length=200) 
#     last_name = models.CharField(max_length=200)
#     time_log = models.TimeField()
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = "Employee"