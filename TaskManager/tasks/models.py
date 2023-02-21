from django.db import models

STATUS_LIST = ((True, 'Zrobione'), (False, 'Niezrobione'))


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Użytkownik: {self.username}"


class Task(models.Model):
    title = models.CharField(max_length=100, default='Tytuł')
    description = models.TextField(max_length=1000, default='Opis', null=True, blank=True)
    status = models.BooleanField(default=False, choices=STATUS_LIST)
    deadline = models.DateTimeField()
    user_key = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tasks")

    def __str__(self):
        return self.title


