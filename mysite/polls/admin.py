from django.contrib import admin
from .models import Feedback
from .models import UserOrder

admin.site.register(UserOrder)
admin.site.register(Feedback)
# Register your models here.
