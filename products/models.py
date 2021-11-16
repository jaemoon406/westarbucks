from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    db_table = 'menus'

class Category(models.Model):
  name = models.CharField(max_length=45)
  menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

  class Meta:
    db_table = 'categories'

class Drink(models.Model):
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  korean_name = models.CharField(max_length=45)
  english_name = models.CharField(max_length=45)
  desciption = models.TextField()

  class Meta:
    db_table = 'drinks'

class Allergy_drink(models.Model):
  allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
  drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

  class Meta:
    db_table = 'allergy_drinks'

class Image(models.Model):
  Drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
  image_url = models.CharField(max_length=2000)

  class Meta:
    db_table = 'images'

class Allergy(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    db_table = 'allergys'
