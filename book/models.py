from django.db import models
# from my_library.models import library_list
from user.models import User

# from user.models import User
class Category(models.Model):
    title=models.CharField()

# Create your models here.
class Booklist(models.Model):
    library = models.ManyToManyField("my_library.librarylist",related_name='lib')
    user = models.ManyToManyField(User,related_name ='my_user' )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    name = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    amount = models.IntegerField()
    book_code = models.IntegerField()
    status = models.BooleanField()
   