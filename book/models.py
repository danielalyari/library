from django.db import models
from my_library.models import library_list
from user.models import User

# Create your models here.
class Book_List(models.Model):
    library = models.ForeignKey(library_list,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    amount = models.IntegerField()
    book_code = models.IntegerField()
    status = models.BooleanField()
   