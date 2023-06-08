from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.CharField()
    text = models.TextField()

class Brand(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class Protein(models.Model):
    price = models.FloatField()
    brand = models.CharField(max_length=20)
    size = models.BigIntegerField()
    flavour = models.CharField(max_length=20)
    grams_of_protein = models.IntegerField()

class Gainer(models.Model):
    price = models.FloatField()
    brand = models.CharField(max_length=20)
    size = models.BigIntegerField()
    flavour = models.CharField(max_length=20)
    kcal = models.IntegerField()

class Creatine(models.Model):
    price = models.FloatField()
    brand = models.CharField(max_length=20)
    size = models.BigIntegerField()
    flavour = models.CharField(max_length=20)

class Bcaa(models.Model):
    price = models.FloatField()
    brand = models.CharField(max_length=20)
    size = models.BigIntegerField()
    flavour = models.CharField(max_length=20)

class Bars(models.Model):
    price = models.FloatField()
    brand = models.CharField(max_length=20)
    size = models.BigIntegerField()
    flavour = models.CharField(max_length=20)
    grams_of_protein = models.IntegerField()
    sugarfree = models.BooleanField()




