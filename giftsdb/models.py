from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField
from django.contrib import admin

class Gift(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=10000)
	home_image = models.ImageField(upload_to='Images/Gifts/')
	expiration_date = models.DateField(null=True, blank=True)
	date_created = models.DateField()
	total_purchases = models.IntegerField(default=0, blank=True)
	price = models.IntegerField()
	vendor = models.ForeignKey('Merchant')
	date_used = models.DateField(blank=True, default=None)
	redeemed = models.BooleanField(default=False)

class Merchant(models.Model):
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=50)
	state = USStateField()
	phone = models.CharField(max_length=150)
	current_gifts = models.ManyToManyField(Gift, related_name='merchant_current_gifts', blank=True)
	past_gifts = models.ManyToManyField(Gift, related_name='merchant_past_gifts', blank=True)
	total_gifts = models.IntegerField(blank=True)
	total_revenues = models.IntegerField(blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Transaction(models.Model):
	purchaser = models.ForeignKey(User, related_name='transactions_purchaser')
	recipient = models.ForeignKey(User, related_name='transactions_recipient')
	coupon_code = models.CharField(max_length=250)
	qr_image = models.ImageField(upload_to='Images/Transactions/QR/')
	gift = models.ForeignKey(Gift)
	total_purchased = models.IntegerField()
	purchase_date = models.DateField()


admin.site.register(Transaction)
admin.site.register(Merchant)
admin.site.register(Gift)

