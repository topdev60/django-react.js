from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def _str_(self):
        return self.name