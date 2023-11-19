# temlatetags/tag_name
# simple_tag

from django import template
from main.models import Category

register = template.Library()


@register.simple_tag() # @register.simple_tag(name='getcats)
def get_category(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

# settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'tag_name': 'app_name.templatetags.tag_name'
            }
        },
    },
]

# html

{% load tag_name %} # {% load name.name-decorator %}
{% tag_fn as var_name %}
{% for i in var_name %}
{% endfor %}


# inclusion_tag

@register.inclusion_tag('template.file')
def show_genres():
    categorys = Category.objects.all()
    return {"categorys": categorys}

# in layout.file =>

{% load tag_name %}

# in template.file =>

{% for category in categorys %}
    {% if select_url == category.pk %}
        <li>{{ category.name }}</li>
    {% else %}
        <li><a href="{{ genre.get_absolute_url }}">{{ category.name }}</a></li>
    {% endif %}
{% endfor %}
