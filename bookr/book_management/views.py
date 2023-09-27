from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views import View

from .forms import BookForm
from .models import Book

class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Rekord modelu Book został zapisany")

