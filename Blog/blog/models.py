from traceback import print_tb
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        print("----------request---------",self)
        queryset = Author.objects.prefetch_related('book_set')
        print("-----------queryset-----------")
        b = []
        for author in queryset:
              print("---------author----------",author)
              
              print("----b----------",b)
              auth = Author.objects.filter(name=self)
            #   print("---------auth----------",auth)
              
              
              print("-----------author-----------",author)
              for book in author.book_set.all():
                 title= book.title
                 print("-----------title-----------",title)
                 b.append(title)
                 print("-----------b-----------",b)
                #  print("----------------1-----------")
                 self.books = b

        super(Author, self).save(*args, **kwargs)
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    
    # def save(self, *args, **kwargs):
    #     # print("----------------------------------",self.title)
    #     queryset = Author.objects.prefetch_related('book_set')
    #     # print("-----------queryset-----------",queryset)
    #     books = []
    #     for author in queryset:
    #         # print("-----------author-----------",author)
    #         for book in author.book_set.all():
    #             # print('-----Book----:',book)
    #             b = Book.objects.filter(author=author).values('title')
    #             print("-----b----",b[0]['title'])
    #             # for i in book:
    #             #     print("-----i----",i)
    #             books.append(book)
    #         # print("-----------books-----------",books)
    #     super(Book, self).save(*args, **kwargs)