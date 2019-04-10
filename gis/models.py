from django.db import models

# Create your models here.
class Marker(models.Model):
    title = models.CharField(max_length=100)
    lng = models.DecimalField(max_digits=9,decimal_places=6)#最大长度和小数最大位数
    lat = models.DecimalField(max_digits=9,decimal_places=6)
    content = models.TextField()
    def __str__(self):
        return self.title

'''
class Detail(models.Model):
    marker = models.ForeignKey(Marker,on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.name
'''
