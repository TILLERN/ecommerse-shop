from django.db import models

# Create your models here.
class About(models.Model):
	article = models.TextField()

	def __str__(self):
		return self.article

class Social_media(models.Model):
    platform = models.CharField(max_length=200)
    link = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.platform


class Phone_number(models.Model):
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.number


class Email(models.Model):
    email_address=models.EmailField(max_length=200)

    def __str__(self):
        return self.email_address

class Physical_address(models.Model):
    name=models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    building = models.CharField(max_length=200, null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name