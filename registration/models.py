from django.db import models
from django.contrib.auth.models import User
from givalittle.giftsdb.models import Gift, Transaction, Merchant
from django.contrib import admin

class UserProfile(models.Model):
	facebook_user = models.BooleanField(default=False)
	facebook_id = models.IntegerField(blank=True)
	user = models.OneToOneField(User)
	total_purchases = models.IntegerField(default=0)
	gifts_purchased = models.ManyToManyField(Gift, blank=True, related_name='user_gifts_purchased')
	gifts_received = models.ManyToManyField(Gift, blank=True, related_name='user_gifts_received')
	is_vendor = models.BooleanField(default=False)
	merchant = models.ForeignKey(Merchant, blank=True, null=True)

admin.site.register(UserProfile)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
