from django.shortcuts import render
from .models import Text


def main_page(request):

    ###### READ #########

    # SELECT * FROM Text;
    # data = Text.objects.all()

    # SELECT * FROM Text WHERE pages > 500;
    # data = Text.objects.filter(pages__gt=500)

    # SELECT * FROM Text WHERE pages <= 500;
    # data = Text.objects.exclude(pages__gt=500)

    # SELECT * FROM Text WHERE id = 3;
    # data = Text.objects.get(id=3)

    ###### INSERT #########

    # INSERT INTO Text (title, anons, full_text, date)
    # Text.objects.create(title='new title',
    #                     anons='new announce',
    #                     full_text='new full_text',
    #                     date='2023-10-09 14:27:54+00:00')

    # var = Text()
    # var.title = 'new title'
    # var.anons = 'new announce'
    # var.full_text = 'new full_text'
    # var.date = '2023-10-09 15:37:54+00:00'
    # var.save()

    ######## UPDATE ##########

    # Text.objects.filter(id__gt=3).update(anons='update announce')

    # data = Text.objects.get(id=6)
    # data.anons = 'update announce'
    # data.save()

    ######### DELETE ###########

    # Text.objects.filter(id__lt=2).delete()

    # data = Text.objects.get(id=5)
    # data.delete()
    # print(data)

    data = Text.objects.order_by('-date')

    return render(request, 'main/index.html', {'data': data})
