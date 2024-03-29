from django.urls import path
from .views import libraryPage, booksPage


urlpatterns = [
    path("library/", libraryPage),
    path("books", booksPage)

]
