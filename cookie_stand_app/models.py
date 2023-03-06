from django.contrib.auth import get_user_model
from django.db import models


class Stand(models.Model):
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    min_customer_per_hour = models.TextField()
    max_customer_per_hour = models.TextField()
    avg_cookie_sales = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'Stand'
