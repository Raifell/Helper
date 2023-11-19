class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = 'Empty'

    class Meta:
        model = Artist
        fields = ['name', 'description', 'photo', 'published', 'genre', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inpert'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('Слишком длинное имя')

        return name

# views.py

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')

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
    <form action="{% url 'add_page' %}" method="post" style="display: flex; flex-direction: column; gap: 10px;" enctype="multipart/form-data">
        {% csrf_token %}
        {% for f in form %}
            <p style="display: flex; gap: 20px;"><label>{{ f.label }}</label>{{ f }}</p>
            <div style="color: red">{{ f.errors }}</div>
        {% endfor %}
        <button type="submit">Add</button>
    </form>
{% endblock %}

################################
# форма через Meta обращается к модели в models.py, формирует поля относительно полей модели fields, указывает атрибуты полей widgets
# __init__ через super().__init() обращается к конструктору родительского класса ModelForm и позволяет менять атрибуты по умолчанию у полей связаных с формой
# clean_name сначала слово clean - обращение к словарю cleandata + название поля модели, для которого идет валидация

# в функции представления не нужно делать проверку на валидность, достаточно использовать метод .save()

# все имеющиеся ошибки в валидации будут выведены через f.errors

#################################
# валидация формы в связке с моделью происходит в два этапа => стандартная проверка .is_valid() => пользовательская проверка после стандартной, clean_name в форме
