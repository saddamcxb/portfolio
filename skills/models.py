from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(help_text="Enter proficiency level as a percentage (0-100)", default=1)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, help_text="FontAwesome icon name or image URL", blank=True)

    def __str__(self):
        return self.name
