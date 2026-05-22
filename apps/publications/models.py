from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=300)
    venue = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
