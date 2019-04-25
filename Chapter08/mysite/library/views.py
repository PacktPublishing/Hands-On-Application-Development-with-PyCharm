from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    latest_books = Book.objects.order_by('-pub_date')[:5]
    context = {'latest_books': latest_books}
    return render(request, 'library/index.html', context)
