from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)
