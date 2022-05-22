from django.test import TestCase
import requests
from django.http import JsonResponse


class GoodAPIViewTests(TestCase):
    def setUp(self):     
        self.base_url = 'http://127.0.0.1:8081/good'

    def test_no_goods(self):
        r = requests.get(self.base_url+'/?id=1/')
        self.assertEqual(r.status_code, 500)

    def test_one_goods(self):
        r = requests.get(self.base_url+'/?id=2/')
        self.assertEqual(r.status_code, 200)   
