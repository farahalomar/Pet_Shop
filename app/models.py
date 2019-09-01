from django.db import models
from django.urls import reverse

class Pet(models.Model):
	name= models.CharField(max_length=50)
	age= models.IntegerField()
	available= models.BooleanField(default=True)
	image= models.ImageField(null=True)
	price= models.DecimalField(decimal_places=2, max_digits= 6)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet-detail', kwargs={'id':self.id})