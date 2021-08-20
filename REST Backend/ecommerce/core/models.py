from django.db import models
import os, uuid
from datetime import datetime


# Create your models here.
class ProductType(models.Model):
    title = models.CharField( max_length=200, null=True)
    def __str__(self):
        return self.title


class Product(models.Model):
    def random_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('product_images/', filename.lower())

    title = models.CharField( max_length=200, blank = True,null=True)
    product_type = models.ForeignKey(ProductType, on_delete = models.DO_NOTHING, blank = True,null=True, related_name="products")
    price = models.IntegerField(blank = True, null=True)
    description = models.TextField(blank = True, null=True)
    image = models.FileField( upload_to=random_file_name, blank = True, null=True)
    priority = models.IntegerField(blank= True, null= True)
    #unit = models.IntegerField(blank=True, null= True)
    def __str__(self):
        return self.title