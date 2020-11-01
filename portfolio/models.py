from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='portfolio/images')
  url = models.URLField(blank=True)
  
  # blank=True allows this field to be nullable
  # when working with images must install Pillow.
  # Step 1. Once you create a model you need to run ./manage.py makemigrations and then ./manage.py migrate this will create the model and then add it as a table in the DB
  # Step 2. To see the newly migrated table in the Django admin dashboard, you need to register the model in the admin.py file.
  
  def __str__(self):
    return self.title
  
  # Returning self.title will allow the title to be display in the initial list of projects in the admin panel