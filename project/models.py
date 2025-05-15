from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.FileField(upload_to="services/")


    def __str__(self):
        return self.title
    