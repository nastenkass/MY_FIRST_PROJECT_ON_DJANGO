from django.db import models

class ImageRecord(models.Model):
    image = models.ImageField(upload_to='polls/media')
    description = models.TextField()
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.description

# Create your models here.

class UserOrder(models.Model):

    SHIPPING_METHOD_CHOICES = (
        ('express', 'Express Shipping'),
        ('regular', 'Regular Shipping'),
        ('free', 'Free Shipping'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('googlepay', 'Google Pay'),
        ('shoppay', 'Shop Pay'),
    )

    email = models.CharField(max_length=50)
    firstname = models.TextField()
    phone = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    adres = models.TextField()
    city = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    delivery = models.CharField(max_length=20, choices=SHIPPING_METHOD_CHOICES)
    credit_1 = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    accept = models.BooleanField(default=False)


class Feedback(models.Model):
    email = models.CharField(max_length=50)
    text = models.TextField()
