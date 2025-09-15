from django.db import models
from book.models import Book_List
from my_library.models import library_list

# Create your models here.
class User(models.Model):
    pers_id=models.IntegerField()
    phonenumber= models.IntegerField()
    library = models.ForeignKey(library_list,on_delete=models.CASCADE)
    book=models.ForeignKey(Book_List,on_delete=models.CASCADE)
    
