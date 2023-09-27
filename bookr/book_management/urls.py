from django.urls import path
from .views import BookCreateView, FormSuccessView

urlpatterns = [
    path('book_record_create', BookCreateView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success')
]