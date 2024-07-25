from django.db import models


# Create your models here.
class Review(models.Model):
    product_name = models.CharField(max_length=100)
    product_review = models.TextField()

    def __str__(self):
        return f"Product Review for {self.product_name}: \n {self.product_review}"
