from django.db import models

# Create your models here






class Coffee(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='coffee')
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)

def __str__(self):
  return self.title
  

class Meta:
  verbose_name = 'coffee'
  verbose_name_plural = 'coffees'