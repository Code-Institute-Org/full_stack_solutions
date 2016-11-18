from django.db import models

STATUS_CHOICES = (
	('1', 'Todo'),
	('2', 'Doing'),
	('3', 'Done')
)


class Todo(models.Model):

	title = models.CharField(max_length=100, null=False)
	description = models.CharField(max_length=255, null=False)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	updated = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title