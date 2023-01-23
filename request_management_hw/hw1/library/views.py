from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output


def book_list(request):
    name = request.GET.get('name') or ''
    author = request.GET.get('author') or ''
    min_price = request.GET.get('min_price') or 0
    max_price = request.GET.get('max_price') or 100000
    

    all_books = Book.objects.filter(name__icontains=name).filter(author__icontains=author)
    all_books = all_books.filter(price__lte=max_price).filter(price__gte=min_price)

    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)
