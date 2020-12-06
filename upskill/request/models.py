from django.db import models

# Create your models here.

class requestUser(models.Model):
	"""docstring for requestUser"""
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length=254)
	company = models.TextField()


class requests(models.Model):

	user = models.ForeignKey(requestUser, on_delete = models.CASCADE)
	topic = models.TextField()
	student_count = models.IntegerField()

		