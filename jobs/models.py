from django.db import models

# Create your models here.
class Job(models.Model):
    # Images of what it looks like, accepts pngs and jpegs
    # Property to save images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)

    def ___str___(self):
        return self.summary