from django.db import models

class Coin(models.Model):
    coin = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.coin} {self.time}'