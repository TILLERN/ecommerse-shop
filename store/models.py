from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cartegory(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	cartegory = models.ForeignKey(Cartegory,on_delete=models.SET_NULL,null=True)
	description = models.TextField()
	price = models.FloatField()
	image = models.ImageField(null=True,upload_to="product_images")
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Customer(models.Model):
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200,null=True)
	phone_number = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.first_name

class Shipping_address(models.Model):
	city_or_town = models.CharField(max_length=200, null=True, blank=True)
	estate = models.CharField(max_length=200, null=True, blank=True)
	street = models.CharField(max_length=200, null=True, blank=True)
	building = models.CharField(max_length=200, null=True, blank=True)
	additional_information = models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.city_or_town)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	shipping_address = models.OneToOneField(Shipping_address, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	is_new = models.BooleanField(default=True)

	def __str__(self):
		return str(self.date_ordered)
		
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total