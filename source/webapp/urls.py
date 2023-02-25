from django.urls import path

from webapp.views.articles import books_view, book_create, book_update, deleted, deleted_confirm

urlpatterns = [
    path('', books_view, name="index_book"),
    path('article', books_view, name="index_book"),
    path('article/create', book_create, name="create_book"),
    path('article/<int:pk>/update', book_update, name="book_update"),
    path('article/<int:pk>/delit', deleted, name="book_delit"),
    path('article/<int:pk>/delit/confirm', deleted_confirm, name="confirm")
]
