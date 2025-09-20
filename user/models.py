from django.db import models
#from my_library.models import libraryList


# Create your models here.
class User(models.Model):
    pers_id=models.IntegerField()
    phonenumber= models.IntegerField()
    library = models.ManyToManyField("my_library.LibraryList",related_name='my_lib',null=True,blank=True)
    book=models.ManyToManyField("book.BookList",related_name='my_book',null=True,blank=True)
    
