from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField(null=True)
    complete=models.BooleanField(default=False,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # class Meta:
    #     ordering=['complete']