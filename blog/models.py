from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"pk": self.pk})