from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Stand


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_stand = Stand.objects.create(location="Bermuda", owner=testuser1, min_customer_per_hour="1", max_customer_per_hour="3", avg_cookie_sales="4")
        test_stand.save()

    def test_things_model(self):
        stand = Stand.objects.get(id=1)
        actual_owner = str(stand.owner)
        actual_location = str(stand.location)
        actual_min_customer_per_hour = str(stand.min_customer_per_hour)
        actual_max_customer_per_hour = str(stand.max_customer_per_hour)
        actual_avg_cookie_sales = str(stand.avg_cookie_sales)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "Bermuda")
        self.assertEqual(actual_min_customer_per_hour, "1")
        self.assertEqual(actual_max_customer_per_hour, "3")
        self.assertEqual(actual_avg_cookie_sales, "4")
