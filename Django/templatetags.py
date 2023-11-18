# temlatetags/tag_name

from django import template
from main.models import Category

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()

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

{% load tag_name %}
{% tag_fn as var_name %}
{% for i in var_name %}
{% endfor %}
