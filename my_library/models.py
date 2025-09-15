from django.db import models
from book.models import Book_List
from user.models import User

# Create your models here.
class library_list(models.Model):
 name= models.CharField()
 lib_code = models.IntegerField()
 city=models.CharField()
 book=models.ForeignKey(Book_List,on_delete=models.CASCADE)
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 