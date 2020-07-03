from django.db import models

# Create your models here.


class Blog(models.Model):
    # 짧은 문자열
    title = models.CharField(max_length=200)
    # date
    pub_date = models.DateTimeField('date published')
    # When you need more length than CharField, you could use TextField
    body = models.TextField()

    def __str__(self):
        return self.title
