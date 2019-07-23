from django.test import TestCase
from shop.models import Notice

class AnimalTestCase(TestCase):
    def setUp(self):
        Notice.objects.create(notice="lion")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        
        lion = Notice.objects.get(notice="lion")
        self.assertIsNotNone(lion)
        # cat = Animal.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')