from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Voucher(models.Model):
    code = models.CharField(max_length=20)
    valid_from = models.DateTimeField(auto_now=True)
    valid_to = models.DateTimeField(auto_now=True)
    trim_voucher = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
