from django.db import models

# Create your models here.
class Student(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.user_id

