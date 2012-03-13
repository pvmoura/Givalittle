from django.db import models
from givalittle.giftsdb.models import Gift, Merchant
from django.contrib.auth.models import User

class Desires(models.Model):
	want = models.TextField(max_length=1500)
	author = models.ForeignKey(User)

