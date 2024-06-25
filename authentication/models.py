from django.db import models

# Create your models here.
class Notes(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    uploadingdate = models.DateTimeField(auto_now=True)
    Description = models.CharField(max_length=100,null =True)
    Name = models.CharField(max_length=30,null =True)
    File = models.FileField(null=True)
    # name = models.CharField(max_length = 200)
    # logo = models.ImageField()
    # description = models.TextField()
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Name)
