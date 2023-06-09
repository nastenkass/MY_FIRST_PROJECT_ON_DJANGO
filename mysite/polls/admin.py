from django.contrib import admin
from .models import Feedback
from .models import UserOrder
from .models import ImageRecord

admin.site.register(UserOrder)
admin.site.register(Feedback)
admin.site.register(ImageRecord)
# Register your models here.
