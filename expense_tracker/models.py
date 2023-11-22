from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename): 
    return f'uploads/{instance.owner.id}/{filename}'
      

# Create your models here.
class Expense(models.Model):
    expense = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    amount = models.DecimalField(
        blank=False,
        default=100.0,
        decimal_places=2,
        max_digits=10,
    )
    date = models.DateTimeField(default=timezone.now, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f'{self.name} - {str(self.amount)}'
    