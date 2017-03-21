from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Notification(models.Model):

	header = models.CharField(max_length=150, validators=[MinLengthValidator(20)])
	content = models.CharField(max_length=300, validators=[MinLengthValidator(20)])
	image_url = models.URLField()
	timing = models.DateTimeField()
	query = models.TextField(validators=[MinLengthValidator(1)])	# WE CANT LEAVE THIS FIELD EMPTY
	is_visit = models.BooleanField(default = True, editable= False)
	def __unicode__(self):
		return self.header
