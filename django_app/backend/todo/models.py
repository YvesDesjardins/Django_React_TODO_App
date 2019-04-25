from django.db import models

# Create your models here.
class Todo(models.Model):
      title = models.TextField()
      completed = models.TextField() # will show completed, in progress or not completed
      dueDate = models.DateTimeField()

      def _str_(self):
        return self.title
