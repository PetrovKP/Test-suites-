from django.test import TestCase

# Create your tests here.

from .models import Test


class SuitesTest(TestCase):

    def test_index(self):
        """Успешное открытие стартовое страницы"""
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_add(self):
        """Проверка добавления теста"""
        resp = self.client.post('/add/', {'name': '', 'run': ''})
        self.assertEqual(resp.status_code, 200)

    def test_add_is_object_in_db(self):
        """Проверка нахождения добавленного теста в бд"""
        resp = self.client.post('/add/', {'name': 'Тест1', 'run': 'python2 run_test.py'})

        test = Test.objects.get(name = 'Тест1')
        self.assertEqual(test.run, 'python2 run_test.py')

    def test_delete (self):
        """Проверка удаления теста"""
        resp = self.client.post('/delete/', {'name': '', 'run': ''})

        self.assertEqual(resp.status_code, 200)

    def test_del_is_object_in_db (self):
        """Проверка удаления добавленного теста из бд"""
        resp = self.client.post('/add/', { 'name': 'Тест1', 'run': 'python2 run_test.py' })

        resp = self.client.post('/delete/', {'name': 'Тест1', 'run': 'python2 run_test.py'})

        tests = Test.objects.all()
        self.assertFalse(tests)
