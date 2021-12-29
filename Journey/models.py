from django.db import models

# Create your models here.
class place(models.Model):
    # id:int we dont need the int as db automatical add it
    city_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pic')
    descri=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=True)