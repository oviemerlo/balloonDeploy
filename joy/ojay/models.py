from django.db import models

# Create your models here.
class Web_edit(models.Model):
    title = models.TextField(default='name of design')
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

