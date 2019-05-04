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

class PaidViewTest(TestCase):
    """Test for PaidView class-view."""
    
    # Test for correct url, which used for response
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('') 
        self.assertEqual(resp.status_code, 200)  
       
    # Test for correst url (access by name)
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paid:pay'))
        self.assertEqual(resp.status_code, 200)

    # Test for using correct template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paid:pay'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paid/index.html')

    # Test for correct reaction by multiple data, sending by user
    def test_view_for_incorrect_input(self):
        resp = self.client.post(reverse('paid:pay'), {'value':"string"})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("errors" in resp.context)

    def test_view_for_too_big_values(self):
        resp = self.client.post(reverse('paid:pay'), {'value':"201"})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("errors" in resp.context)


    def test_view_for_too_small_values(self):
        resp = self.client.post(reverse('paid:pay'), {'value':"-0.00012"})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("errors" in resp.context)
