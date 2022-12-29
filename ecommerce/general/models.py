from django.db import models


class App(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_upcoming = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppImages(models.Model):
    app = models.ForeignKey(App,
                            related_name="image",
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = ImageField(upload_to='upload/images/general/app-images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)