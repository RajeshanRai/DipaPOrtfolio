from django.db import models


class CVDownload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f"CVDownload {self.created:%Y-%m-%d %H:%M:%S}"
