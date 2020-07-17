from django.db import models

# Create your models here.


class Portfolio(models.Model):
    # 짧은 문자열
    title = models.CharField(max_length=255)
    # date
    image = models.ImageField(upload_to='images/')
    # When you need more length than CharField, you could use TextField
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
