from django.db import models
from book.models import Booklist
from user.models import User

# Create your models here.
class libraryList(models.Model):
 name= models.CharField()
 lib_code = models.IntegerField()
 city=models.CharField()
 book=models.ManyToManyField(Booklist,related_name='books')
 user=models.ManyToManyField(User,related_name='users')
 