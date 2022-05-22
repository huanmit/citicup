from django.test import TestCase
import requests


# 单元测试示例
class GoodAPIViewTests(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8081/good'

    def test_no_goods(self):
        r = requests.get(self.base_url+'/?id=1/')
        self.assertEqual(r.status_code, 500)

    def test_one_goods(self):
        r = requests.get(self.base_url+'/?id=2/')
        self.assertEqual(r.status_code, 200)


# 基本路径测试-获得成就
class AchievementAPIViewTests(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8081/achievements'

    def test_no_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951120')
        walker = r.json()[0]
        self.assertEqual(walker, 0)

    def test_bronze_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951121')
        walker = r.json()[0]
        self.assertEqual(walker, 1)

    def test_silver_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951122')
        walker = r.json()[0]
        self.assertEqual(walker, 2)

    def test_gold_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951123')
        print(r.json())
        walker = r.json()[0]
        self.assertEqual(walker, 3)


# 基本路径测试-举报
class ReportAPIViewTests(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8081/achievements'

    def test_no_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951120')
        walker = r.json()[0]
        self.assertEqual(walker, 0)

    def test_bronze_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951121')
        walker = r.json()[0]
        self.assertEqual(walker, 1)

    def test_silver_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951122')
        walker = r.json()[0]
        self.assertEqual(walker, 2)

    def test_gold_achievements(self):
        r = requests.get(self.base_url+'?user_id=1951123')
        print(r.json())
        walker = r.json()[0]
        self.assertEqual(walker, 3)
