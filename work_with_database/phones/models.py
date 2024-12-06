from django.db import models


class Phone(models.Model):
            #id = models.CharField(max_length=50, primary_key = True)
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=50, decimal_places=2)
            image = models.CharField()
            release_date = models.DateField(auto_now=False, auto_now_add=False)
            lte_exists = models.BooleanField(null=False)
            slug = models.CharField(max_length = 80, unique=True)
