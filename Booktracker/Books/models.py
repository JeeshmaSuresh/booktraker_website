from django.db import models

# Create your models here.
class Books(models.Model):
      status=[
        ('Read','Read'),
        ('Currently Reading','Curently Readding'),
        ('Want to Read','Want to Read'),
      ]
      title=models.CharField(max_length=100)
      author=models.CharField(max_length=100)
      description=models.CharField(max_length=350)
      date=models.DateField(auto_now=True)
      status=models.CharField(max_length=30,choices=status,default='WR')
