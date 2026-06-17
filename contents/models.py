from django.db import models

# Create your models here.
class Channel(models.Model):
    name=models.CharField(max_length=255)
    logo=models.URLField()
    subscription_count= models.IntegerField(default=0)
    discription=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Video_Content(models.Model):
    title=models.CharField(max_length=255)
    thumbnail=models.URLField()
    channel=models.ForeignKey(Channel, on_delete=models.CASCADE)
    views_count=models.IntegerField(default=0)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    @property
    def formatted_views(self):
        if self.views_count >= 1000000:
            return f"{self.views_count / 1000000:.1f}M"
        elif self.views_count >= 1000:
            return f"{self.views_count / 1000:.1f}K"
        return str(self.views_count)

class Shorts(models.Model):
    title=models.CharField(max_length=255)
    thumbnail=models.URLField()
    channel=models.ForeignKey(Channel, on_delete=models.CASCADE)
    views_count=models.IntegerField(default=0)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    @property
    def formatted_views(self):
        if self.views_count >= 1000000:
            return f"{self.views_count / 1000000:.1f}M"
        elif self.views_count >= 1000:
            return f"{self.views_count / 1000:.1f}K"
        return str(self.views_count)

    def __str__ (self):
        return self.title
