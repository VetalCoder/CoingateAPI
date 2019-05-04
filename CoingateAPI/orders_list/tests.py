"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from django.urls import reverse

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class OrdersViewTest(TestCase):
    """Test for OrdersView class-view."""
    
    # Test for correct url, which used for response
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/orders') 
        self.assertEqual(resp.status_code, 301)
        
    # Test for correct url, which used for response with params
    def test_view_url_exists_at_desired_location_with_params(self): 
        resp = self.client.get('/orders?page=3') 
        self.assertEqual(resp.status_code, 301)
       
    # Test for correst url (access by name)
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('orders_list:orders'))
        self.assertEqual(resp.status_code, 200)

    # Test for using correct template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('orders_list:orders'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'orders_list/index.html')

    # Test for contains data
    def test_view_contains_data_in_response(self):
        resp = self.client.get(reverse('orders_list:orders'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("orders" in resp.context)
        self.assertTrue("pages" in resp.context)
        self.assertTrue("selected_page" in resp.context)


class OrdersDetailViewTest(TestCase):
    """Test for OrdersDetailView class-view."""

    # Test for uncorrect url, which used for response
    def test_view_uncorrect_urls(self): 
        resp = self.client.get('/orders/42') 
        self.assertEqual(resp.status_code, 301)

        resp = self.client.get('/orders/string') 
        self.assertEqual(resp.status_code, 404)
        

    # Test for uncorrest url (access by name)
    def test_view_uncorrect_urls_accessible_by_name(self):
        resp = self.client.get(reverse('orders_list:detail', kwargs={'order_id':'42'}))
        self.assertEqual(resp.status_code, 404)

    # Test for using correct template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('orders_list:detail', kwargs={'order_id':'184367'}))
        self.assertTemplateUsed(resp, 'orders_list/detail.html')

    # Test for correct answer for some urls
    def test_view_answers(self):
        resp = self.client.get(reverse('orders_list:detail', kwargs={'order_id':'184367'}))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('orders_list:detail', kwargs={'order_id':'18436721'}))
        self.assertEqual(resp.status_code, 404)
