from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('Todo', 'Todo'),
    ('Doing', 'Doing'),
    ('Done', 'Done')
)


class Todo(models.Model):

    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
