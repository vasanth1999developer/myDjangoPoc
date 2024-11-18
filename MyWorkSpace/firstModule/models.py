from django.db import models

# Create your models here.
class Products(models.Model):
       
       
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        deleted_at = models.DateTimeField(null=True)
        is_deleted = models.BooleanField(default=False)
        
        def __str__(self):
                return self.name
         