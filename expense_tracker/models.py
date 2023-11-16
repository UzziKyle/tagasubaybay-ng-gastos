from django.db import models
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100, blank=False)
    amount = models.DecimalField(
        blank=False,
        default=100.0,
        decimal_places=2,
        max_digits=10,
    )
    date = models.DateTimeField(default=timezone.now, blank=False)
    
    def __str__(self):
        return str(self.amount)
    