from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    


class Education(models.Model):
    degree = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False, blank=True)
    end_date = models.DateField(auto_now_add=False, blank=True)
    institution = models.CharField(max_length=200)
    institution_url = models.URLField(default="")

    def __str__(self):
        return self.degree

