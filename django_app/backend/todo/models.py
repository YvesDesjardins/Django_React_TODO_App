from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.TextField()
    completed = models.TextField()  # will show todo/in-progress/done
    dueDate = models.DateField()

    def _str_(self):
        return self.title
