from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    test_title = 'Todo test title'
    test_body = 'Todo test body'

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title=TodoModelTest.test_title, body=TodoModelTest.test_body)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, TodoModelTest.test_title)

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, TodoModelTest.test_body)
