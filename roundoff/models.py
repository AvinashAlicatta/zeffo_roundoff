from django.db import models

# Create your models here.


class UserSettings(models.Model):
    user_id = models.IntegerField(primary_key=True, default=0)
    round_up = models.IntegerField(default=0)
    multiplier = models.IntegerField(blank=True, null=True)


class Transactions(models.Model):
    user_id = models.ForeignKey(UserSettings, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    merchant_name = models.CharField(max_length=30)
    transaction_money = models.FloatField(default=None)





