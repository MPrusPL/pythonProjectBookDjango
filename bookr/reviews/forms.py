from django import forms
from .models import Publisher, Review, Book

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=(('title', 'Tytuł'), ('contributor', 'Współtwórca'), ('publisher', 'Wydawca')))

class NewsletterSignupForm(forms.Form):
    signup = forms.BooleanField(label='Chcesz otrzymywać newsletter?', required=False)
    email = forms.EmailField(help_text='Wpisz adres email, aby się zapisać', required=False)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['signup'] and not cleaned_data.get('email'):
            self.add_error('email', 'Jeśli chcesz się zapisać, musisz podać adres email.')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('date_edited', 'book')
    rating = forms.IntegerField(min_value=0, max_value=5)

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['cover', 'sample']