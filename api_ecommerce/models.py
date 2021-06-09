from django.db import models


class Product(models.Model):
    category = (
        ('Electronic', 'Electronic'),
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
    )
    availability = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(choices=category, max_length=255)
    availability = models.CharField(choices=availability, max_length=255)
    price = models.FloatField()
    img_url = models.ImageField(upload_to="product-ecom-images")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ecom-product"
