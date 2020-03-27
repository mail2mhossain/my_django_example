from django.forms import ModelForm, Textarea
from library_app.models import Book, Author
from django.utils.translation import gettext_lazy as _

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
