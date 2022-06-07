from django.db import models

class ExtraNotice(models.Model):
    title = models.CharField(max_length = 200,blank=False,null=True)
    url = models.URLField(max_length = 1000,blank=False,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.title}"
