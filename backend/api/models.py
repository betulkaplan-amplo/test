from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=50)
    registry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
