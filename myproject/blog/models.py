from statistics import mode
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True)
    created_data = models.DateTimeField(auto_now_add = True)
    published_data = models.DateTimeField(blank =True, null = True)

    def __str__(self) :
        return self.title

    def publish(self) :
        self.published_data = timezone.now()
        self.save()

    def hide(self) :
        self.publisehd_data = None
        self.save()






