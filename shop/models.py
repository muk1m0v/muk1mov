from django.db import models

class Shops(models.Model):
    title = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Debts(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=9)
    price = models.IntegerField()
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, related_name='debts')

    def __str__(self):
        return self.name

