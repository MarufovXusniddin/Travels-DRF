from django.db import models

# Create your models here.


class Klass(models.Model):
    type = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.type


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    term = models.CharField(max_length=50)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name