from django.db import models
from django.conf import settings

class Heritage(models.Model):
    k_name = models.CharField(max_length=50)
    h_name = models.CharField(max_length=50)
    content = models.TextField()
    imageurl = models.URLField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    era = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150)
    clsfc_code = models.IntegerField()
    clsfc_name = models.CharField(max_length=50)
    sido = models.CharField(max_length=50)
    hit = models.IntegerField(null=True, default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_heritages', blank=True)
    visit_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='visited_heritages', blank=True)
    dib_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dibs_heritages', blank=True)

class Heritage_picture(models.Model):
    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE)
    imageurl = models.URLField()


class Tag(models.Model):
    name = models.CharField(max_length=100)
    tagging = models.ManyToManyField(Heritage, related_name='tag_heritages', blank=True)