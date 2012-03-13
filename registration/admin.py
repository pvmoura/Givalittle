from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from givalittle.registration.models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
	model = UserProfile

class UserProfileAdmin(UserAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
	inlines = [UserProfileInline]


admin.site.register(User, UserProfileAdmin)
