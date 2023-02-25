from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Book

from webapp.forms import BookForm

from webapp.models import StatusChoice


def books_view(request: WSGIRequest):
    books = Book.objects.filter(status=StatusChoice.ACTIVE).order_by("-create_at")
    context = {
        "books": books
    }
    return render(request, "books.html", context=context)


def book_create(request: WSGIRequest):
    if request.method == "GET":
        form = BookForm()
        return render(request, "book_create.html", context={"form": form})
    form = BookForm(data=request.POST)
    if not form.is_valid():
        return render(request, "book_create.html", context={"form": form})
    else:
        book = Book.objects.create(**form.cleaned_data)
        return redirect("index_book")


def book_update(request: WSGIRequest, pk):
    book = get_object_or_404(Book, pk=pk)
    book.update()
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index_book")
        return render(request, "book_update.html", context={"form": form, "book": book})
    form = BookForm(instance=book)
    return render(request, "book_update.html", context={"form": form, "book": book})


def deleted(request: WSGIRequest, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "delete_confirm.html", context={
        'book': book
    })


def deleted_confirm(request: WSGIRequest, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("index_book")
