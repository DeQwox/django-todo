from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTests(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="Test Description", completed=False)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertTrue(task.created_at)

class TaskViewTests(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_list.html')

    def test_task_creation_view(self):
        response = self.client.post(reverse('task_list'), {
            'title': 'New Task',
            'description': 'New Description',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'New Task')