from django.test import TestCase
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer
from django.urls import reverse


class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = APIClient()

        # Add test instances of the Menu model
        self.menu_item1 = Menu.objects.create(
            Title='Pasta', Price=12.99, Inventory=50)
        self.menu_item2 = Menu.objects.create(
            Title='Burger', Price=9.99, Inventory=20)
        self.menu_item3 = Menu.objects.create(
            Title='Salad', Price=7.99, Inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)
