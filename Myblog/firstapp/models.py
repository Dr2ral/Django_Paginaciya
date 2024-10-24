from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=1, max_digits=5, blank=False)
    size = models.DecimalField(decimal_places=1, max_digits=4, blank=False)
    description = models.TextField()


