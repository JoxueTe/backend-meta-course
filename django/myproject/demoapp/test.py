from django.test import TestCase
from datetime import datetime
from .models import Menu
from .models import MenuCategory


class MenuModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cat = MenuCategory.objects.create(menu_Category_name="Italian")
        cls.menu = Menu.objects.create(
            menu_item = "Spaguetti",
            price = 5,
            category_id = cat
        )

    def test_fields(self):

        self.assertIsInstance(self.menu.menu_item, str)

        self.assertIsInstance(self.menu.price, int)

   