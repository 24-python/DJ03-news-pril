from .models import Full_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class Full_postForm(ModelForm):
    class Meta:
        model = Full_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'autor']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Короткая новость'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            'autor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'})
        }

