from django.db import models

class Consumer(models.Model):
	company=models.CharField(max_length=250)
	reference=models.CharField(max_length=250)
	email=models.CharField(max_length=500)
	phone_number=models.TextField()
	
	
class Request(models.Model):
	consumer=models.ForeignKey(Consumer, on_delete=models.CASCADE)
	number_of_requests=models.IntegerField()
	type_of_programes=models.CharField(max_length=100)
