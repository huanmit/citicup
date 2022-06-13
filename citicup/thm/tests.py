from ast import walk
from django.test import TestCase #unittest pyunit
import requests
from django.db import models


# Create your tests here.
class StepUploadTest(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/wxsteps_upload'

    #POST插入一条微信步数信息
    def test_upload_step(self):
        form_data = {
            "userID": "admin",
            "plogTypeID": 1,
            "appId": "wx6ad063cf9aa46a3c",
            "sessionKey": "Z3GoT9H8tZHOuc/RMVEoQA==",
            "encryptedData": "cs69PnsM3zan5N54ydygrwCLmTiadOh0xcxUq9n8fZmVxurq15jh+En94qFZyfuvvPoAifNCwEeP0kyLafW4GlfNubO9iokzpRN8Oz1TOKlVru/+ryBgiPNnpjMZNiKbWgSo0y3OwjGDHwdIbpJtrC+IcMoryBzfnZrMK2wvxV/rFCQNZtdQz6cYOg2GGy80oLn5G1M9zpdJ27ts2YEYb4j9PDRPfa4dc/03Y8DSWwX/4iEoD0UrzrPJ0S9rvpXkH6eU8Bocrnk44fGJm5YRIPOz9P4aJe1iD/7UUBkSxkK693WqN2Om4S3gj9QSo91Ng6fZs8k7N42getCL4rqdTew8kqx8qx3AHJp7oAUaQdW7QJQcHn/q9uCmxw4PAcl2DOuIb3OQoGEIarbh2s22hHo2yR65LMiuVEeou61oAxtRpl3DtkEXwBF2whXzjy3Q+M8jRYqkQMMJ1sQwDlOTTX1+zK9Qe997ZT98/6pnS1azX/8WT4c9WyNGX9eCJ7idvgJEQP15zESiGsSPoOuAFivNHtdfeNB+z5VoBWxQuxFRHExngpi94COJ6S8QoHnXw3BqvKu5WhGasStnH4aY2BxWcTXZR4nBR7TcPhv/Lk3MsDiZ2G8yjbRACTDkUuSGrFC+I+PXMfX/Rmv0Pve5gX7wh7zDWCCsYvj5LLU2szQ2YXdr61cQxK4V2kfb1APpB33WKi8r+sysCebYsIEQ1yU/CgIWlqWgPDgfCw9qwBJ1DA/K/tM959ysX/AuTANgHi7IAm29UCQi6bkkF9BAGIi8QPp3TOKKteSpFFpleqyJM/Csj7ZqHheenqha3JyA2rwPCMqjj7AEdAf74Zu6XpUALAfFweHJbl2AfrhvR/EZQED5fVObc6oFPmqpr7Gafy4b4x2SumAkGGShOKbHR6ro2NNM/TPzCoyWF8657gqd3ZPFs2nKHT5ySrUWz1KO6bQKjmepg3M9PJbDQ09YEWO0R4MHDubyCl75UhXxwEt+PaRjSQvdZ9EKsw9wLjL+vnClR8DrG5zvLmVKp1DtQRPaABaKMBmfKkEdrVZBJhmzDUjNIYMgg5x1iXr/0yqMqsOKB1KTgC9B1C0CpPgrmpHvRdC1FqW6mZkK0qZRSORrKz9MstpIk8HjFWDLSFwu0+hUqApeLZX4XeAL98JnsdJ3wcSBJOvg5cdZPfNYNAz2QvgF83dpwJ3cqFJ8SXgvM7uDcAFjklV5IVRuBgon0d1QnaYfuwepZGWOraZV8KuNTu1ttNPAfdJSgrtSDcW2F15tOM2+h9PrmanmJQvxbjxJImmDvEYnYc6ZBZRNlRkUiTATVVCYNAL0G09NFCmFVGpUQr1A7V+CO6OXgoFvKItjZ/6fSZCgE4jcP45rjhd0Ms7M60hyqjVC+ribFyvhuxtetI6ZA8OGk2ddadXiclzYn0S4VSmDoclO5KL5ne1tn7z3G9tZlh5h26VqOdJ8ZuZooz5oNdwbGi/MOpPP8vIi+3UZXSoa6WyfcNehF9zTX8qYv6JseRi5csBRlrXLwwLfk5aFJ0Gf95kSzUxzc0VEbRJs9k9c3VvcfmbuLgCV+J/OmkDrtQrrc3SIMY3P16JRVKS9mg9ItKK9+0xY8Ee5tIXOLLTm8CpCIQZ0KsWOhD5aZWRjKGHX4dCExoQF",
            "iv": "byorsokJujbJCToy1Gy5Gw=="
        }
        
        r = requests.post(self.base_url+'/',data=form_data)
        result = r.json()

class AchievementTest(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/achievements'

    def test_no_achievements(self):
        r = requests.get(self.base_url + '?user_id=admin')
        walker = r.json()[0]
        self.assertEqual(walker,0)

    def test_bronze_achievements(self):
        r = requests.get(self.base_url + '?user_id=florrie')
        walker = r.json()[0]
        self.assertEqual(walker,1)

    def test_bronze_achievements(self):
        r = requests.get(self.base_url + '?user_id=citi')
        walker = r.json()[0]
        self.assertEqual(walker,2)

    