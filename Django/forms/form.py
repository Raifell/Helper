from django import forms
from .models import *


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label='Имя', widget=forms.TextInput(attrs={'class': 'inpert'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    published = forms.BooleanField(label='Публикация', required=False, initial=True)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанр', empty_label='Жанр')
    slug = forms.SlugField(max_length=255, label='Ссылка')


# views.py

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print()
            print(form.cleaned_data)
            try:
                Artist.objects.create(**form.cleaned_data)
                return redirect('main_page')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()

    context = {
        'title': 'Add page',
        'menu': menu,
        'form': form,
    }
    return render(request, 'music/index_addpage.html', context=context)

# html

{% block content %}
    <h1>{{ title }}</h1>
    <form action="{% url 'add_page' %}" method="post" style="display: flex; flex-direction: column; gap: 10px;">
        {% csrf_token %}
        <div style="color: red;">{{ form.non_field_errors }}</div>
        {% for f in form %}
            <p style="display: flex; gap: 20px;"><label>{{ f.label }}</label>{{ f }}</p>
            <div style="color: red">{{ f.errors }}</div>
        {% endfor %}
        <button type="submit">Add</button>
    </form>
{% endblock %}

######################################

# в случае, если метод POST => проверка на валидность данных => попытка записи в БД, если данные не валидны => вызов ошибки и передача в .non_field_errors - ошибки не связаные с полями
