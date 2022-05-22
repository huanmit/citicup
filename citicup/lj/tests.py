from django.test import TestCase
import requests
from django.db import models


class GoodAPIViewTests(TestCase):
    def setUp(self):
        class Good(models.Model):
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')
        self.base_url = 'http://127.0.0.1:8081/good'

    def test_no_goods(self):
        r = requests.get(self.base_url+'/?=1/')
        self.assertEqual(r.status_code, 500)
