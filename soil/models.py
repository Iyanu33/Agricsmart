from django.db import models
from django.db import models
from django.contrib.auth.models import User

class SoilImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='soil_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return f"{self.user.username} - {self.prediction}"
# Create your models here.
