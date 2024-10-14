from django.db import models

# Create your models here.
#class Post(models.Model):
#    title = models.CharField(max_length=100)
#    content = models.TextField()
#    created_at = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=1, max_digits=5, blank=False)
    size = models.DecimalField(decimal_places=1, max_digits=4, blank=False)
    description = models.TextField()


