from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        """Création d'un utilisateur de test et d'une tâche"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(title="Tâche test", completed=False, priority=2, user=self.user)

    def test_task_creation(self):
        """Vérifie que la tâche est bien créée"""
        self.assertEqual(self.task.title, "Tâche test")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.priority, 2)
        self.assertEqual(self.task.user.username, "testuser")

    def test_task_str(self):
        """Vérifie que la représentation de la tâche est correcte"""
        self.assertEqual(str(self.task), "Tâche test - Moyenne")


class ViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_home_page(self):
        """Vérifie que la page d'accueil fonctionne"""
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_todo_list_redirect_if_not_logged_in(self):
        """Vérifie que la redirection fonctionne pour les utilisateurs non connectés"""
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 302)  # Redirection vers login

    def test_todo_list_logged_in(self):
        """Vérifie que l'utilisateur connecté accède bien à sa Todo List"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)


class AuthTest(TestCase):

    def test_register_page(self):
        """Vérifie que la page d'inscription fonctionne"""
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        """Test l'inscription d'un nouvel utilisateur"""
        response = self.client.post('/register/', {
            'username': 'newuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Doit rediriger après inscription
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_valid_user(self):
        """Vérifie qu'un utilisateur valide peut se connecter"""
        User.objects.create_user(username="validuser", password="testpassword")
        response = self.client.post('/login/', {
            'username': 'validuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Doit rediriger après connexion
