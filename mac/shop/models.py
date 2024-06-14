from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.autoField()
    product_name = models.CharField(max_length = 50)
    description = models.CharField(max_length=300)
    pub_date = models.DateField()