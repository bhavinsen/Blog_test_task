from django.shortcuts import render

from .forms import BookForm

# Create your views here.

from .models import Author, Book
from django.db.models import Count
from django.http import HttpResponse
 
 
def list_view(request):
  
    context ={}
 
    #4.1 function for print the book title and the author name (who wrote it) for all the books
    authors = Author.objects.all()
    context['dataset'] = Book.objects.filter(author__in=authors).values('title', 'author__name')
    
    #4.2 function for print the author’s name and all the books he wrote.
    queryset = Author.objects.prefetch_related('book_set')
        
    for author in queryset:
    
        for book in author.book_set.all():
            print('Book: {}'.format(book))
    
    book_list = Book.objects.all()
    
    # function for the author’s name and the number of books he wrote. Order by the number of books written, descending
    authors = Author.objects.filter(book__in=book_list
          ).annotate(num_books=Count('id')).order_by('-num_books')
             
    context['queryset']=queryset
    context['authors']=authors  
    return render(request, "book_view.html", context)


def book_view(request):
    print("-0-------book_view----------")
    context = {}
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        print("-0-------form----------",form.errors)
        if form.is_valid():
            print("-0-------if----------")
            form.save()
            return HttpResponse('Data Saved')
        else:
            return HttpResponse('Invalid form')
    else:
        form = BookForm()
    context['form'] = form
    return render(request, 'book.html', context)